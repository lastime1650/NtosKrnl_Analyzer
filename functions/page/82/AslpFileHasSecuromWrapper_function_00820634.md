# AslpFileHasSecuromWrapper

- RVA: `0x00820634`–`0x008206AA` (길이 `118` bytes)
- VA: `0x0000000140820634`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C954`
- 디코드: `36`개 명령, `118/118` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0082067C` → [strncmp](../../text/6C/strncmp_function_006C6720.md) (function, `0x006C6720`)

### Direct callers
- [AslpFileGetExeWrapper](../81/AslpFileGetExeWrapper_function_0081EAF4.md) at `0x0081EB6B`

### Static image references
- `0x00820672` → RVA `0x000400C8` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0082067C` → [strncmp](../../text/6C/strncmp_function_006C6720.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00820634  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00820639  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
0082063E  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
00820643  57                              push rdi
00820644  48 83 EC 20                     sub rsp, 0x20
00820648  0F B7 41 14                     movzx eax, word ptr [rcx + 0x14]
0082064C  48 8D 79 18                     lea rdi, [rcx + 0x18]
00820650  33 DB                           xor ebx, ebx
00820652  48 8B E9                        mov rbp, rcx
00820655  48 03 F8                        add rdi, rax
00820658  8B F3                           mov esi, ebx
0082065A  0F B7 45 06                     movzx eax, word ptr [rbp + 6]
0082065E  3B F0                           cmp esi, eax
00820660  73 30                           jae 0x140820692
00820662  39 5F 0C                        cmp dword ptr [rdi + 0xc], ebx
00820665  74 1E                           je 0x140820685
00820667  39 5F 08                        cmp dword ptr [rdi + 8], ebx
0082066A  74 19                           je 0x140820685
0082066C  41 B8 08 00 00 00               mov r8d, 8
00820672  48 8D 15 4F FA 81 FF            lea rdx, [rip - 0x7e05b1]
00820679  48 8B CF                        mov rcx, rdi
0082067C  E8 9F 60 EA FF                  call 0x1406c6720
00820681  85 C0                           test eax, eax
00820683  74 08                           je 0x14082068d
00820685  FF C6                           inc esi
00820687  48 83 C7 28                     add rdi, 0x28
0082068B  EB CD                           jmp 0x14082065a
0082068D  BB 01 00 00 00                  mov ebx, 1
00820692  48 8B 6C 24 38                  mov rbp, qword ptr [rsp + 0x38]
00820697  8B C3                           mov eax, ebx
00820699  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
0082069E  48 8B 74 24 40                  mov rsi, qword ptr [rsp + 0x40]
008206A3  48 83 C4 20                     add rsp, 0x20
008206A7  5F                              pop rdi
008206A8  C3                              ret
008206A9  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall AslpFileHasSecuromWrapper(__int64 a1)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (32);
    v_rbx = 0;
    v_rdi = (a1 + 24) + (*(unsigned __int16 *)(a1 + 20));
loc_0082065A:
    if (0 >= ((unsigned int)(*(unsigned __int16 *)(a1 + 6)))) goto loc_00820692;
    if ((*(unsigned int *)(v_rdi + 12)) == 0) goto loc_00820685;
    if ((*(unsigned int *)(v_rdi + 8)) == 0) goto loc_00820685;
    result = strncmp(v_rdi, v_rip - 8258993, 8, a4);
    if ((unsigned int)(result) == 0) goto loc_0082068D;
loc_00820685:
    v_rsi = (unsigned int)((0) + 1);
    v_rdi = (v_rdi) + (40);
    goto loc_0082065A;
loc_0082068D:
loc_00820692:
    v_rsp = (v_rsp) + (32);
    return 1;
}
```

## 5. (Beta) C Style

```c
int64_t AslpFileHasSecuromWrapper(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (32);
    local_rbx = 0;
    local_rdi = (Arg1 + 24) + (*(uint16_t *)(arg1 + 0x14));
loc_0082065A:
    if (0 >= ((uint32_t)(*(uint16_t *)(arg1 + 0x6)))) goto loc_00820692;
    if ((*(uint32_t *)(local_rdi + 0xC)) == 0) goto loc_00820685;
    if ((*(uint32_t *)(local_rdi + 0x8)) == 0) goto loc_00820685;
    result = strncmp(local_rdi, v_rip - 8258993, 8, a4);
    if ((uint32_t)(result) == 0) goto loc_0082068D;
loc_00820685:
    local_rsi = (uint32_t)((0) + 1);
    local_rdi = (local_rdi) + (40);
    goto loc_0082065A;
loc_0082068D:
loc_00820692:
    local_rsp = (local_rsp) + (32);
    return 1;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x6` | `16` | `R` |
| `Arg1` | `+ 0x8` | `32` | `R` |
| `Arg1` | `+ 0xC` | `32` | `R` |
| `Arg1` | `+ 0x14` | `16` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00820634&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00820634[BB_00820634]
  bb_0082065A[BB_0082065A]
  bb_00820662[BB_00820662]
  bb_00820667[BB_00820667]
  bb_0082066C[BB_0082066C]
  bb_00820685[BB_00820685]
  bb_0082068D[BB_0082068D]
  bb_00820692[BB_00820692]
  bb_008206A9[BB_008206A9]
  bb_00820634 -->|flow| bb_0082065A
  bb_0082065A -->|branch| bb_00820692
  bb_0082065A -->|fallthrough| bb_00820662
  bb_00820662 -->|branch| bb_00820685
  bb_00820662 -->|fallthrough| bb_00820667
  bb_00820667 -->|branch| bb_00820685
  bb_00820667 -->|fallthrough| bb_0082066C
  bb_0082066C -->|branch| bb_0082068D
  bb_0082066C -->|fallthrough| bb_00820685
  bb_00820685 -->|branch| bb_0082065A
  bb_0082068D -->|flow| bb_00820692
```

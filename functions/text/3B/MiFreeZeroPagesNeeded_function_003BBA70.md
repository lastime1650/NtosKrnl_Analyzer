# MiFreeZeroPagesNeeded

- RVA: `0x003BBA70`–`0x003BBAE4` (길이 `116` bytes)
- VA: `0x00000001403BBA70`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00088864`
- 디코드: `33`개 명령, `116/116` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x003BBA9B` → [MiNodeFreeZeroPages](MiNodeFreeZeroPages_function_003BBF60.md) (function, `0x003BBF60`)
- `0x003BBAB3` → [MiGetNodeStandbyPageCount](MiGetNodeStandbyPageCount_function_003BC09C.md) (function, `0x003BC09C`)

### Direct callers
- [MiRebalanceZeroFreeLists](MiRebalanceZeroFreeLists_function_003BB9B0.md) at `0x003BB9E8`
- [MiPruneStandbyPages](MiPruneStandbyPages_function_003BC0E4.md) at `0x003BC29E`
- [MiPruneStandbyPages](MiPruneStandbyPages_function_003BC0E4.md) at `0x003BC3C1`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003BBA70  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
003BBA75  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
003BBA7A  57                              push rdi
003BBA7B  48 83 EC 20                     sub rsp, 0x20
003BBA7F  8B DA                           mov ebx, edx
003BBA81  48 8B F1                        mov rsi, rcx
003BBA84  41 8A F8                        mov dil, r8b
003BBA87  41 B8 00 00 08 00               mov r8d, 0x80000
003BBA8D  48 69 CB 80 DF 00 00            imul rcx, rbx, 0xdf80
003BBA94  40 8A D7                        mov dl, dil
003BBA97  48 03 4E 10                     add rcx, qword ptr [rsi + 0x10]
003BBA9B  E8 C0 04 00 00                  call 0x1403bbf60
003BBAA0  4C 8B D8                        mov r11, rax
003BBAA3  48 3D 00 02 00 00               cmp rax, 0x200
003BBAA9  73 35                           jae 0x1403bbae0
003BBAAB  44 8A C7                        mov r8b, dil
003BBAAE  8B D3                           mov edx, ebx
003BBAB0  48 8B CE                        mov rcx, rsi
003BBAB3  E8 E4 05 00 00                  call 0x1403bc09c
003BBAB8  33 D2                           xor edx, edx
003BBABA  B9 00 04 00 00                  mov ecx, 0x400
003BBABF  49 2B CB                        sub rcx, r11
003BBAC2  48 3D 00 10 00 00               cmp rax, 0x1000
003BBAC8  48 0F 42 CA                     cmovb rcx, rdx
003BBACC  48 8B C1                        mov rax, rcx
003BBACF  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
003BBAD4  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
003BBAD9  48 83 C4 20                     add rsp, 0x20
003BBADD  5F                              pop rdi
003BBADE  C3                              ret
003BBADF  CC                              int3
003BBAE0  33 C0                           xor eax, eax
003BBAE2  EB EB                           jmp 0x1403bbacf
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiFreeZeroPagesNeeded(__int64 a1, int a2, unsigned __int8 a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_rsp = (v_rsp) - (32);
    a1 = (a1) * ((unsigned int)(a2));
    a1 = (a1) + (*(unsigned __int64 *)(a1 + 16));
    result = MiNodeFreeZeroPages(a1, a3, (unsigned int)(0x80000ULL), a4);
    if (result >= 512) goto loc_003BBAE0;
    result = MiGetNodeStandbyPageCount(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    a2 = 0;
    a1 = ((unsigned int)(0x400ULL)) - (result);
    if (result < 0x1000ULL) { a1 = 0; }
loc_003BBACF:
    v_rsp = (v_rsp) + (32);
    return a1;
loc_003BBAE0:
    result = 0;
    goto loc_003BBACF;
}
```

## 5. (Beta) C Style

```c
void *MiFreeZeroPagesNeeded(void *Arg1, int32_t Arg2, uint8_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    local_rsp = (local_rsp) - (32);
    Arg1 = (Arg1) * ((uint32_t)(Arg2));
    Arg1 = (Arg1) + (*(uint64_t *)(arg1 + 0x10));
    result = MiNodeFreeZeroPages(Arg1, Arg3, (uint32_t)(0x80000ULL), a4);
    if (result >= 512) goto loc_003BBAE0;
    result = MiGetNodeStandbyPageCount(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, a4);
    Arg2 = 0;
    Arg1 = ((uint32_t)(0x400ULL)) - (result);
    if (result < 0x1000ULL) { Arg1 = 0; }
loc_003BBACF:
    local_rsp = (local_rsp) + (32);
    return Arg1;
loc_003BBAE0:
    result = 0;
    goto loc_003BBACF;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x10` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003BBA70&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003BBA70[BB_003BBA70]
  bb_003BBAAB[BB_003BBAAB]
  bb_003BBACF[BB_003BBACF]
  bb_003BBADF[BB_003BBADF]
  bb_003BBAE0[BB_003BBAE0]
  bb_003BBA70 -->|branch| bb_003BBAE0
  bb_003BBA70 -->|fallthrough| bb_003BBAAB
  bb_003BBAAB -->|flow| bb_003BBACF
  bb_003BBADF -->|flow| bb_003BBAE0
  bb_003BBAE0 -->|branch| bb_003BBACF
```

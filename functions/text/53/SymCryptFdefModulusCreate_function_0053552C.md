# SymCryptFdefModulusCreate

- RVA: `0x0053552C`–`0x005355A2` (길이 `118` bytes)
- VA: `0x000000014053552C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C954`
- 디코드: `36`개 명령, `118/118` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0053554E` → [SymCryptFdefSizeofModulusFromDigits](SymCryptFdefSizeofModulusFromDigits_function_00535728.md) (function, `0x00535728`)
- `0x00535584` → [SymCryptFdefDivisorCreate](SymCryptFdefDivisorCreate_function_005358DC.md) (function, `0x005358DC`)

### Direct callers
- [SymCryptModulusCreate](../52/SymCryptModulusCreate_function_00525CF4.md) at `0x00525CF8`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0053552C  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00535531  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
00535536  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
0053553B  57                              push rdi
0053553C  48 83 EC 20                     sub rsp, 0x20
00535540  48 8B D9                        mov rbx, rcx
00535543  41 8B F8                        mov edi, r8d
00535546  41 8B C8                        mov ecx, r8d
00535549  48 8B EA                        mov rbp, rdx
0053554C  33 F6                           xor esi, esi
0053554E  E8 D5 01 00 00                  call 0x140535728
00535553  8B C8                           mov ecx, eax
00535555  85 C0                           test eax, eax
00535557  74 30                           je 0x140535589
00535559  48 3B E9                        cmp rbp, rcx
0053555C  72 2B                           jb 0x140535589
0053555E  83 63 0C 00                     and dword ptr [rbx + 0xc], 0
00535562  48 8D 55 C0                     lea rdx, [rbp - 0x40]
00535566  89 4B 08                        mov dword ptr [rbx + 8], ecx
00535569  44 8B C7                        mov r8d, edi
0053556C  8B CF                           mov ecx, edi
0053556E  C7 03 00 00 4D 67               mov dword ptr [rbx], 0x674d0000
00535574  C1 E1 06                        shl ecx, 6
00535577  48 8B F3                        mov rsi, rbx
0053557A  89 4B 10                        mov dword ptr [rbx + 0x10], ecx
0053557D  48 8D 4B 40                     lea rcx, [rbx + 0x40]
00535581  89 7B 04                        mov dword ptr [rbx + 4], edi
00535584  E8 53 03 00 00                  call 0x1405358dc
00535589  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
0053558E  48 8B C6                        mov rax, rsi
00535591  48 8B 74 24 40                  mov rsi, qword ptr [rsp + 0x40]
00535596  48 8B 6C 24 38                  mov rbp, qword ptr [rsp + 0x38]
0053559B  48 83 C4 20                     add rsp, 0x20
0053559F  5F                              pop rdi
005355A0  C3                              ret
005355A1  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SymCryptFdefModulusCreate(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (32);
    v_rsi = 0;
    result = SymCryptFdefSizeofModulusFromDigits((unsigned int)(a3), a2, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_00535589;
    if (a2 >= ((unsigned int)((unsigned int)(result)))) {
        a2 = a2 - 64;
        *(unsigned int *)(a1 + 8) = (unsigned int)((unsigned int)((unsigned int)(result)));
        a3 = (unsigned int)((unsigned int)(a3));
        a1 = (unsigned int)((unsigned int)(a3));
        *(unsigned int *)(a1) = 0x674D0000ULL;
        a1 = (unsigned int)((a1) << (6));
        v_rsi = a1;
        *(unsigned int *)(a1 + 16) = (unsigned int)(a1);
        a1 = a1 + 64;
        *(unsigned int *)(a1 + 4) = (unsigned int)((unsigned int)(a3));
        result = SymCryptFdefDivisorCreate(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (32);
    return v_rsi;
}
```

## 5. (Beta) C Style

```c
int64_t SymCryptFdefModulusCreate(void *Arg1, int64_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (32);
    local_rsi = 0;
    result = SymCryptFdefSizeofModulusFromDigits((uint32_t)(Arg3), Arg2, Arg3, a4);
    if ((uint32_t)(result) == 0) goto loc_00535589;
    if (Arg2 >= ((uint32_t)((uint32_t)(result)))) {
        Arg2 = Arg2 - 64;
        *(uint32_t *)(arg1 + 0x8) = (uint32_t)((uint32_t)((uint32_t)(result)));
        Arg3 = (uint32_t)((uint32_t)(Arg3));
        Arg1 = (uint32_t)((uint32_t)(Arg3));
        *(uint32_t *)(arg1) = 0x674D0000ULL;
        Arg1 = (uint32_t)((Arg1) << (6));
        local_rsi = Arg1;
        *(uint32_t *)(arg1 + 0x10) = (uint32_t)(Arg1);
        Arg1 = Arg1 + 64;
        *(uint32_t *)(arg1 + 0x4) = (uint32_t)((uint32_t)(Arg3));
        result = SymCryptFdefDivisorCreate(Arg1, Arg2, Arg3, a4);
    }
    local_rsp = (local_rsp) + (32);
    return local_rsi;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `W` |
| `Arg1` | `+ 0x4` | `32` | `W` |
| `Arg1` | `+ 0x8` | `32` | `W` |
| `Arg1` | `+ 0xC` | `32` | `R/W` |
| `Arg1` | `+ 0x10` | `32` | `W` |
| `Arg1` | `+ 0x40` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0053552C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0053552C[BB_0053552C]
  bb_00535559[BB_00535559]
  bb_0053555E[BB_0053555E]
  bb_00535589[BB_00535589]
  bb_005355A1[BB_005355A1]
  bb_0053552C -->|branch| bb_00535589
  bb_0053552C -->|fallthrough| bb_00535559
  bb_00535559 -->|branch| bb_00535589
  bb_00535559 -->|fallthrough| bb_0053555E
  bb_0053555E -->|flow| bb_00535589
```

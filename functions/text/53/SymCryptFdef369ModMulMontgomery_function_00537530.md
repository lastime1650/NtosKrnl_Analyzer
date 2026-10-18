# SymCryptFdef369ModMulMontgomery

- RVA: `0x00537530`–`0x0053757F` (길이 `79` bytes)
- VA: `0x0000000140537530`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000794E0`
- 디코드: `23`개 명령, `79/79` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0053755B` → [SymCryptFdef369RawMulAsm](SymCryptFdef369RawMulAsm_function_0053B5D0.md) (function, `0x0053B5D0`)
- `0x00537569` → [SymCryptFdef369MontgomeryReduceAsm](SymCryptFdef369MontgomeryReduceAsm_function_0053B6F0.md) (function, `0x0053B6F0`)

### Direct callers
- [SymCryptFdef369ModSquareMontgomery](SymCryptFdef369ModSquareMontgomery_function_00537690.md) at `0x005376A9`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00537530  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00537535  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
0053753A  57                              push rdi
0053753B  48 83 EC 30                     sub rsp, 0x30
0053753F  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
00537544  48 8B C2                        mov rax, rdx
00537547  8B 51 04                        mov edx, dword ptr [rcx + 4]
0053754A  49 8B F1                        mov rsi, r9
0053754D  48 8B F9                        mov rdi, rcx
00537550  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00537555  44 8B CA                        mov r9d, edx
00537558  48 8B C8                        mov rcx, rax
0053755B  E8 70 40 00 00                  call 0x14053b5d0
00537560  4C 8B C6                        mov r8, rsi
00537563  48 8B D3                        mov rdx, rbx
00537566  48 8B CF                        mov rcx, rdi
00537569  E8 82 41 00 00                  call 0x14053b6f0
0053756E  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
00537573  48 8B 74 24 48                  mov rsi, qword ptr [rsp + 0x48]
00537578  48 83 C4 30                     add rsp, 0x30
0053757C  5F                              pop rdi
0053757D  C3                              ret
0053757E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SymCryptFdef369ModMulMontgomery(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_rsp = (v_rsp) - (48);
    v_stack_m18 = a5;
    result = SymCryptFdef369RawMulAsm(a2, (unsigned int)(*(unsigned int *)(a1 + 4)), a3, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)))));
    result = SymCryptFdef369MontgomeryReduceAsm(a1, a5, a4, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)))));
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SymCryptFdef369ModMulMontgomery(void *Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    local_rsp = (local_rsp) - (48);
    v_stack_m18 = Arg5;
    result = SymCryptFdef369RawMulAsm(Arg2, (uint32_t)(*(uint32_t *)(arg1 + 0x4)), Arg3, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)))));
    result = SymCryptFdef369MontgomeryReduceAsm(Arg1, Arg5, Arg4, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)))));
    local_rsp = (local_rsp) + (48);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x4` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00537530&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00537530[BB_00537530]
  bb_0053757E[BB_0053757E]
```

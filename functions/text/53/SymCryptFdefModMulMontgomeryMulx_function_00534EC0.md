# SymCryptFdefModMulMontgomeryMulx

- RVA: `0x00534EC0`–`0x00534F0F` (길이 `79` bytes)
- VA: `0x0000000140534EC0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000794E0`
- 디코드: `23`개 명령, `79/79` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00534EEB` → [SymCryptFdefRawMulMulx](../52/SymCryptFdefRawMulMulx_function_0052E1F0.md) (function, `0x0052E1F0`)
- `0x00534EF9` → [SymCryptFdefMontgomeryReduceMulx](../52/SymCryptFdefMontgomeryReduceMulx_function_0052F2E0.md) (function, `0x0052F2E0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00534EC0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00534EC5  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
00534ECA  57                              push rdi
00534ECB  48 83 EC 30                     sub rsp, 0x30
00534ECF  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
00534ED4  48 8B C2                        mov rax, rdx
00534ED7  8B 51 04                        mov edx, dword ptr [rcx + 4]
00534EDA  49 8B F1                        mov rsi, r9
00534EDD  48 8B F9                        mov rdi, rcx
00534EE0  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00534EE5  44 8B CA                        mov r9d, edx
00534EE8  48 8B C8                        mov rcx, rax
00534EEB  E8 00 93 FF FF                  call 0x14052e1f0
00534EF0  4C 8B C6                        mov r8, rsi
00534EF3  48 8B D3                        mov rdx, rbx
00534EF6  48 8B CF                        mov rcx, rdi
00534EF9  E8 E2 A3 FF FF                  call 0x14052f2e0
00534EFE  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
00534F03  48 8B 74 24 48                  mov rsi, qword ptr [rsp + 0x48]
00534F08  48 83 C4 30                     add rsp, 0x30
00534F0C  5F                              pop rdi
00534F0D  C3                              ret
00534F0E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SymCryptFdefModMulMontgomeryMulx(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5)
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
    result = SymCryptFdefRawMulMulx(a2, (unsigned int)(*(unsigned int *)(a1 + 4)), a3, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)))));
    result = SymCryptFdefMontgomeryReduceMulx(a1, a5, a4, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)))));
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SymCryptFdefModMulMontgomeryMulx(void *Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5)
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
    result = SymCryptFdefRawMulMulx(Arg2, (uint32_t)(*(uint32_t *)(arg1 + 0x4)), Arg3, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)))));
    result = SymCryptFdefMontgomeryReduceMulx(Arg1, Arg5, Arg4, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)))));
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

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00534EC0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00534EC0[BB_00534EC0]
  bb_00534F0E[BB_00534F0E]
```

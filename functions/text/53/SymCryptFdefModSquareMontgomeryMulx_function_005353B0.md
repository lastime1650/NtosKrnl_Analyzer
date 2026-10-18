# SymCryptFdefModSquareMontgomeryMulx

- RVA: `0x005353B0`–`0x005353F8` (길이 `72` bytes)
- VA: `0x00000001405353B0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060BC4`
- 디코드: `22`개 명령, `72/72` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x005353D4` → [SymCryptFdefRawSquareMulx](../52/SymCryptFdefRawSquareMulx_function_0052E830.md) (function, `0x0052E830`)
- `0x005353E2` → [SymCryptFdefMontgomeryReduceMulx](../52/SymCryptFdefMontgomeryReduceMulx_function_0052F2E0.md) (function, `0x0052F2E0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005353B0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
005353B5  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
005353BA  57                              push rdi
005353BB  48 83 EC 20                     sub rsp, 0x20
005353BF  48 8B C2                        mov rax, rdx
005353C2  49 8B D8                        mov rbx, r8
005353C5  8B 51 04                        mov edx, dword ptr [rcx + 4]
005353C8  48 8B F9                        mov rdi, rcx
005353CB  48 8B C8                        mov rcx, rax
005353CE  4D 8B C1                        mov r8, r9
005353D1  49 8B F1                        mov rsi, r9
005353D4  E8 57 94 FF FF                  call 0x14052e830
005353D9  4C 8B C3                        mov r8, rbx
005353DC  48 8B D6                        mov rdx, rsi
005353DF  48 8B CF                        mov rcx, rdi
005353E2  E8 F9 9E FF FF                  call 0x14052f2e0
005353E7  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
005353EC  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
005353F1  48 83 C4 20                     add rsp, 0x20
005353F5  5F                              pop rdi
005353F6  C3                              ret
005353F7  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SymCryptFdefModSquareMontgomeryMulx(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_rsp = (v_rsp) - (32);
    result = SymCryptFdefRawSquareMulx(a2, (unsigned int)(*(unsigned int *)(a1 + 4)), a4, a4);
    result = SymCryptFdefMontgomeryReduceMulx(a1, a4, a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SymCryptFdefModSquareMontgomeryMulx(void *Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    local_rsp = (local_rsp) - (32);
    result = SymCryptFdefRawSquareMulx(Arg2, (uint32_t)(*(uint32_t *)(arg1 + 0x4)), Arg4, Arg4);
    result = SymCryptFdefMontgomeryReduceMulx(Arg1, Arg4, Arg3, Arg4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x4` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005353B0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005353B0[BB_005353B0]
  bb_005353F7[BB_005353F7]
```

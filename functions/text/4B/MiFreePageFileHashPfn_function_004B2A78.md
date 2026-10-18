# MiFreePageFileHashPfn

- RVA: `0x004B2A78`–`0x004B2ACB` (길이 `83` bytes)
- VA: `0x00000001404B2A78`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `20`개 명령, `83/83` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004B2AC0` → [MiInsertPageInFreeOrZeroedList](../33/MiInsertPageInFreeOrZeroedList_function_00334D20.md) (function, `0x00334D20`)

### Direct callers
- [MiFreePageFileHashPfns](../2D/MiFreePageFileHashPfns_function_002DBEF8.md) at `0x002DBF82`
- [MiMapPageFileHash](../49/MiMapPageFileHash_function_004921E0.md) at `0x004926A5`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004B2A78  48 83 EC 28                     sub rsp, 0x28
004B2A7C  48 8D 14 49                     lea rdx, [rcx + rcx*2]
004B2A80  48 C1 E2 04                     shl rdx, 4
004B2A84  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
004B2A8E  48 03 D0                        add rdx, rax
004B2A91  49 B8 00 00 00 00 00 00 00 C0   movabs r8, 0xc000000000000000
004B2A9B  48 8B 42 18                     mov rax, qword ptr [rdx + 0x18]
004B2A9F  49 23 C0                        and rax, r8
004B2AA2  48 89 42 18                     mov qword ptr [rdx + 0x18], rax
004B2AA6  8B 42 20                        mov eax, dword ptr [rdx + 0x20]
004B2AA9  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
004B2AAD  33 C0                           xor eax, eax
004B2AAF  66 89 44 24 30                  mov word ptr [rsp + 0x30], ax
004B2AB4  8B 44 24 30                     mov eax, dword ptr [rsp + 0x30]
004B2AB8  89 42 20                        mov dword ptr [rdx + 0x20], eax
004B2ABB  BA 02 00 00 00                  mov edx, 2
004B2AC0  E8 5B 22 E8 FF                  call 0x140334d20
004B2AC5  48 83 C4 28                     add rsp, 0x28
004B2AC9  C3                              ret
004B2ACA  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiFreePageFileHashPfn(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_p8;

    v_rsp = (v_rsp) - (40);
    a2 = (a1 + a1 * 2) << (4);
    a2 = (a2) + (result);
    result = (*(unsigned __int64 *)(a2 + 24)) & (a3);
    *(unsigned __int64 *)(a2 + 24) = result;
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 32)));
    result = 0;
    v_stack_p8 = 0;
    *(unsigned int *)(a2 + 32) = (unsigned int)((unsigned int)(v_stack_p8));
    result = MiInsertPageInFreeOrZeroedList(a1, 2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiFreePageFileHashPfn(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    a2 = (Arg1 + Arg1 * 2) << (4);
    a2 = (a2) + (result);
    result = (*(uint64_t *)(a2 + 0x18)) & (a3);
    *(uint64_t *)(a2 + 0x18) = result;
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(a2 + 0x20)));
    result = 0;
    v_stack_p8 = 0;
    *(uint32_t *)(a2 + 0x20) = (uint32_t)((uint32_t)(v_stack_p8));
    result = MiInsertPageInFreeOrZeroedList(Arg1, 2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0 + rcx*2` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004B2A78&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004B2A78[BB_004B2A78]
  bb_004B2ACA[BB_004B2ACA]
```

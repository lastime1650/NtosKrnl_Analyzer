# RtlEthernetAddressToStringA

- RVA: `0x005EBDE0`–`0x005EBE44` (길이 `100` bytes)
- VA: `0x00000001405EBDE0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008A2AC`
- 디코드: `26`개 명령, `100/100` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x005EBE2E` → [sprintf_s](../50/sprintf_s_function_00505E40.md) (function, `0x00505E40`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x005EBE19` → RVA `0x006CCBC0` (` ?? ::FNODOBFM::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005EBDE0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
005EBDE5  57                              push rdi
005EBDE6  48 83 EC 50                     sub rsp, 0x50
005EBDEA  44 0F B6 41 04                  movzx r8d, byte ptr [rcx + 4]
005EBDEF  48 8B FA                        mov rdi, rdx
005EBDF2  0F B6 41 05                     movzx eax, byte ptr [rcx + 5]
005EBDF6  BA 12 00 00 00                  mov edx, 0x12
005EBDFB  44 0F B6 51 03                  movzx r10d, byte ptr [rcx + 3]
005EBE00  44 0F B6 59 02                  movzx r11d, byte ptr [rcx + 2]
005EBE05  0F B6 59 01                     movzx ebx, byte ptr [rcx + 1]
005EBE09  44 0F B6 09                     movzx r9d, byte ptr [rcx]
005EBE0D  48 8B CF                        mov rcx, rdi
005EBE10  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
005EBE14  44 89 44 24 38                  mov dword ptr [rsp + 0x38], r8d
005EBE19  4C 8D 05 A0 0D 0E 00            lea r8, [rip + 0xe0da0]
005EBE20  44 89 54 24 30                  mov dword ptr [rsp + 0x30], r10d
005EBE25  44 89 5C 24 28                  mov dword ptr [rsp + 0x28], r11d
005EBE2A  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
005EBE2E  E8 0D A0 F1 FF                  call 0x140505e40
005EBE33  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
005EBE38  48 98                           cdqe
005EBE3A  48 03 C7                        add rax, rdi
005EBE3D  48 83 C4 50                     add rsp, 0x50
005EBE41  5F                              pop rdi
005EBE42  C3                              ret
005EBE43  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlEthernetAddressToStringA(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_m18;
    unsigned int v_stack_m20;
    unsigned int v_stack_m28;
    unsigned int v_stack_m30;
    unsigned int v_stack_m38;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (80);
    v_stack_m18 = (unsigned int)(*(unsigned __int8 *)(a1 + 5));
    v_stack_m20 = (unsigned int)(*(unsigned __int8 *)(a1 + 4));
    v_stack_m28 = (unsigned int)(*(unsigned __int8 *)(a1 + 3));
    v_stack_m30 = (unsigned int)(*(unsigned __int8 *)(a1 + 2));
    v_stack_m38 = (unsigned int)(*(unsigned __int8 *)(a1 + 1));
    result = sprintf_s(a2, 18, v_rip + 920992, *(unsigned __int8 *)(a1));
    result = (result) + (a2);
    v_rsp = (v_rsp) + (80);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t RtlEthernetAddressToStringA(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_m18;
    uint32_t v_stack_m20;
    uint32_t v_stack_m28;
    uint32_t v_stack_m30;
    uint32_t v_stack_m38;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (80);
    v_stack_m18 = (uint32_t)(*(uint8_t *)(arg1 + 0x5));
    v_stack_m20 = (uint32_t)(*(uint8_t *)(arg1 + 0x4));
    v_stack_m28 = (uint32_t)(*(uint8_t *)(arg1 + 0x3));
    v_stack_m30 = (uint32_t)(*(uint8_t *)(arg1 + 0x2));
    v_stack_m38 = (uint32_t)(*(uint8_t *)(arg1 + 0x1));
    result = sprintf_s(Arg2, 18, v_rip + 920992, *(uint8_t *)(arg1));
    result = (result) + (Arg2);
    local_rsp = (local_rsp) + (80);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `8` | `R` |
| `Arg1` | `+ 0x1` | `8` | `R` |
| `Arg1` | `+ 0x2` | `8` | `R` |
| `Arg1` | `+ 0x3` | `8` | `R` |
| `Arg1` | `+ 0x4` | `8` | `R` |
| `Arg1` | `+ 0x5` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005EBDE0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005EBDE0[BB_005EBDE0]
  bb_005EBE43[BB_005EBE43]
```

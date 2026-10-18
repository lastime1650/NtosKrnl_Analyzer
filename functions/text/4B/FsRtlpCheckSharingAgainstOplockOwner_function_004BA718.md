# FsRtlpCheckSharingAgainstOplockOwner

- RVA: `0x004BA718`–`0x004BA7AA` (길이 `146` bytes)
- VA: `0x00000001404BA718`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BB4A8`
- 디코드: `43`개 명령, `146/146` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004BA798` → [IoCheckLinkShareAccess](../../page/9A/IoCheckLinkShareAccess_function_009A4180.md) (function, `0x009A4180`)

### Direct callers
- [FsRtlpOplockBreakByCacheFlags](../4E/FsRtlpOplockBreakByCacheFlags_function_004E4990.md) at `0x004E51C9`
- [FsRtlpOplockBreakByCacheFlags](../4E/FsRtlpOplockBreakByCacheFlags_function_004E4990.md) at `0x004E538E`
- [FsRtlpOplockBreakByCacheFlags](../4E/FsRtlpOplockBreakByCacheFlags_function_004E4990.md) at `0x004E5B96`
- [FsRtlpOplockBreakByCacheFlags](../4E/FsRtlpOplockBreakByCacheFlags_function_004E4990.md) at `0x004E65F1`
- [FsRtlpOplockBreakByCacheFlags](../4E/FsRtlpOplockBreakByCacheFlags_function_004E4990.md) at `0x004E6922`
- [FsRtlpOplockBreakByCacheFlags](../4E/FsRtlpOplockBreakByCacheFlags_function_004E4990.md) at `0x004E6A47`
- [FsRtlpOplockBreakByCacheFlags](../4E/FsRtlpOplockBreakByCacheFlags_function_004E4990.md) at `0x004E6BB8`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x004BA798` → [IoCheckLinkShareAccess](../../page/9A/IoCheckLinkShareAccess_function_009A4180.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004BA718  48 83 EC 58                     sub rsp, 0x58
004BA71C  48 8B 81 B8 00 00 00            mov rax, qword ptr [rcx + 0xb8]
004BA723  45 8B D0                        mov r10d, r8d
004BA726  33 C9                           xor ecx, ecx
004BA728  4C 8B C2                        mov r8, rdx
004BA72B  38 08                           cmp byte ptr [rax], cl
004BA72D  75 74                           jne 0x1404ba7a3
004BA72F  38 4A 4A                        cmp byte ptr [rdx + 0x4a], cl
004BA732  8B C1                           mov eax, ecx
004BA734  C7 44 24 28 02 00 00 00         mov dword ptr [rsp + 0x28], 2
004BA73C  0F 95 C0                        setne al
004BA73F  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
004BA744  38 4A 4B                        cmp byte ptr [rdx + 0x4b], cl
004BA747  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
004BA74B  8B C1                           mov eax, ecx
004BA74D  0F 95 C0                        setne al
004BA750  C7 44 24 30 01 00 00 00         mov dword ptr [rsp + 0x30], 1
004BA758  38 4A 4C                        cmp byte ptr [rdx + 0x4c], cl
004BA75B  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
004BA75F  8B C1                           mov eax, ecx
004BA761  0F 95 C0                        setne al
004BA764  38 4A 4D                        cmp byte ptr [rdx + 0x4d], cl
004BA767  89 44 24 3C                     mov dword ptr [rsp + 0x3c], eax
004BA76B  8B C1                           mov eax, ecx
004BA76D  0F 95 C0                        setne al
004BA770  38 4A 4E                        cmp byte ptr [rdx + 0x4e], cl
004BA773  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
004BA777  8B C1                           mov eax, ecx
004BA779  0F 95 C0                        setne al
004BA77C  38 4A 4F                        cmp byte ptr [rdx + 0x4f], cl
004BA77F  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
004BA783  8B C1                           mov eax, ecx
004BA785  0F 95 C0                        setne al
004BA788  41 0F B7 D1                     movzx edx, r9w
004BA78C  4C 8D 4C 24 30                  lea r9, [rsp + 0x30]
004BA791  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
004BA795  41 8B CA                        mov ecx, r10d
004BA798  E8 E3 99 4E 00                  call 0x1409a4180
004BA79D  48 83 C4 58                     add rsp, 0x58
004BA7A1  C3                              ret
004BA7A2  CC                              int3
004BA7A3  B8 0D 00 00 C0                  mov eax, 0xc000000d
004BA7A8  EB F3                           jmp 0x1404ba79d
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall FsRtlpCheckSharingAgainstOplockOwner(__int64 a1, __int64 a2, int a3, unsigned __int16 a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_m10;
    unsigned int v_stack_m14;
    unsigned int v_stack_m18;
    unsigned int v_stack_m1C;
    unsigned int v_stack_m20;
    unsigned int v_stack_m24;
    unsigned int v_stack_m28;
    unsigned int v_stack_m30;
    unsigned __int64 v_stack_m38;

    v_rsp = (v_rsp) - (88);
    a1 = 0;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 184))) != 0) goto loc_004BA7A3;
    v_stack_m30 = 2;
    result = ((*(unsigned __int8 *)(a2 + 74)) != 0) ? 1 : 0;
    v_stack_m38 = 0;
    v_stack_m24 = (unsigned int)(result);
    result = ((*(unsigned __int8 *)(a2 + 75)) != 0) ? 1 : 0;
    v_stack_m28 = 1;
    v_stack_m20 = (unsigned int)(result);
    result = ((*(unsigned __int8 *)(a2 + 76)) != 0) ? 1 : 0;
    v_stack_m1C = (unsigned int)(result);
    result = ((*(unsigned __int8 *)(a2 + 77)) != 0) ? 1 : 0;
    v_stack_m18 = (unsigned int)(result);
    result = ((*(unsigned __int8 *)(a2 + 78)) != 0) ? 1 : 0;
    v_stack_m14 = (unsigned int)(result);
    result = ((*(unsigned __int8 *)(a2 + 79)) != 0) ? 1 : 0;
    v_stack_m10 = (unsigned int)(result);
    result = IoCheckLinkShareAccess((unsigned int)((unsigned int)((unsigned int)(a3))), a4, a2, v_stack_m28);
loc_004BA79D:
    v_rsp = (v_rsp) + (88);
    return result;
loc_004BA7A3:
    goto loc_004BA79D;
}
```

## 5. (Beta) C Style

```c
int64_t FsRtlpCheckSharingAgainstOplockOwner(void *Arg1, void *Arg2, int32_t Arg3, uint16_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_m10;
    uint32_t v_stack_m14;
    uint32_t v_stack_m18;
    uint32_t v_stack_m1C;
    uint32_t v_stack_m20;
    uint32_t v_stack_m24;
    uint32_t v_stack_m28;
    uint32_t v_stack_m30;
    uint64_t v_stack_m38;

    local_rsp = (local_rsp) - (88);
    Arg1 = 0;
    if ((*(uint8_t *)(*(uint64_t *)(arg1 + 0xB8))) != 0) goto loc_004BA7A3;
    v_stack_m30 = 2;
    result = ((*(uint8_t *)(arg2 + 0x4A)) != 0) ? 1 : 0;
    v_stack_m38 = 0;
    v_stack_m24 = (uint32_t)(result);
    result = ((*(uint8_t *)(arg2 + 0x4B)) != 0) ? 1 : 0;
    v_stack_m28 = 1;
    v_stack_m20 = (uint32_t)(result);
    result = ((*(uint8_t *)(arg2 + 0x4C)) != 0) ? 1 : 0;
    v_stack_m1C = (uint32_t)(result);
    result = ((*(uint8_t *)(arg2 + 0x4D)) != 0) ? 1 : 0;
    v_stack_m18 = (uint32_t)(result);
    result = ((*(uint8_t *)(arg2 + 0x4E)) != 0) ? 1 : 0;
    v_stack_m14 = (uint32_t)(result);
    result = ((*(uint8_t *)(arg2 + 0x4F)) != 0) ? 1 : 0;
    v_stack_m10 = (uint32_t)(result);
    result = IoCheckLinkShareAccess((uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg4, Arg2, v_stack_m28);
loc_004BA79D:
    local_rsp = (local_rsp) + (88);
    return result;
loc_004BA7A3:
    goto loc_004BA79D;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xB8` | `64` | `R` |
| `Arg2` | `+ 0x4A` | `8` | `R` |
| `Arg2` | `+ 0x4B` | `8` | `R` |
| `Arg2` | `+ 0x4C` | `8` | `R` |
| `Arg2` | `+ 0x4D` | `8` | `R` |
| `Arg2` | `+ 0x4E` | `8` | `R` |
| `Arg2` | `+ 0x4F` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004BA718&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004BA718[BB_004BA718]
  bb_004BA72F[BB_004BA72F]
  bb_004BA79D[BB_004BA79D]
  bb_004BA7A2[BB_004BA7A2]
  bb_004BA7A3[BB_004BA7A3]
  bb_004BA718 -->|branch| bb_004BA7A3
  bb_004BA718 -->|fallthrough| bb_004BA72F
  bb_004BA72F -->|flow| bb_004BA79D
  bb_004BA7A2 -->|flow| bb_004BA7A3
  bb_004BA7A3 -->|branch| bb_004BA79D
```

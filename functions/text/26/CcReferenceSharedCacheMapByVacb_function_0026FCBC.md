# CcReferenceSharedCacheMapByVacb

- RVA: `0x0026FCBC`–`0x0026FD39` (길이 `125` bytes)
- VA: `0x000000014026FCBC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00065960`
- 디코드: `33`개 명령, `125/125` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0026FCF2` → [KeAcquireInStackQueuedSpinLockAtDpcLevel](../27/KeAcquireInStackQueuedSpinLockAtDpcLevel_function_00275740.md) (function, `0x00275740`)
- `0x0026FD25` → [KeReleaseInStackQueuedSpinLockFromDpcLevel](../21/KeReleaseInStackQueuedSpinLockFromDpcLevel_function_002171B0.md) (function, `0x002171B0`)

### Direct callers
- [CcUnmapInactiveViewsInternal](../27/CcUnmapInactiveViewsInternal_function_0027174C.md) at `0x00271970`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0026FCBC  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0026FCC1  57                              push rdi
0026FCC2  48 83 EC 40                     sub rsp, 0x40
0026FCC6  33 C0                           xor eax, eax
0026FCC8  48 8D 54 24 20                  lea rdx, [rsp + 0x20]
0026FCCD  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0026FCD2  48 8B D9                        mov rbx, rcx
0026FCD5  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
0026FCD9  0F 57 C0                        xorps xmm0, xmm0
0026FCDC  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
0026FCE1  40 32 FF                        xor dil, dil
0026FCE4  48 8B 88 18 02 00 00            mov rcx, qword ptr [rax + 0x218]
0026FCEB  48 81 C1 00 03 00 00            add rcx, 0x300
0026FCF2  E8 49 5A 00 00                  call 0x140275740
0026FCF7  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
0026FCFB  48 8B 41 60                     mov rax, qword ptr [rcx + 0x60]
0026FCFF  48 83 E0 F0                     and rax, 0xfffffffffffffff0
0026FD03  48 8B 40 28                     mov rax, qword ptr [rax + 0x28]
0026FD07  48 39 48 08                     cmp qword ptr [rax + 8], rcx
0026FD0B  75 13                           jne 0x14026fd20
0026FD0D  8B 41 04                        mov eax, dword ptr [rcx + 4]
0026FD10  BF 01 00 00 00                  mov edi, 1
0026FD15  FF C0                           inc eax
0026FD17  89 41 04                        mov dword ptr [rcx + 4], eax
0026FD1A  01 B9 20 02 00 00               add dword ptr [rcx + 0x220], edi
0026FD20  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0026FD25  E8 86 74 FA FF                  call 0x1402171b0
0026FD2A  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
0026FD2F  40 8A C7                        mov al, dil
0026FD32  48 83 C4 40                     add rsp, 0x40
0026FD36  5F                              pop rdi
0026FD37  C3                              ret
0026FD38  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CcReferenceSharedCacheMapByVacb(__int64 a1)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (64);
    result = 0;
    v_stack_m18 = 0;
    v_stack_m28 = v_xmm0;
    v_rdi = 0;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 536)) + (768);
    result = KeAcquireInStackQueuedSpinLockAtDpcLevel(a1, v_stack_m28, a3, a4);
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 96)) & (-16);
    result = *(unsigned __int64 *)(result + 40);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 40) + 8)) == (*(unsigned __int64 *)(a1 + 8))) {
        result = *(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 4);
        v_rdi = 1;
        result = (unsigned int)((result) + 1);
        *(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 4) = (unsigned int)(result);
    }
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(v_stack_m28, v_stack_m28, a3, a4);
    v_rsp = (v_rsp) + (64);
    return (unsigned __int8)(v_rdi);
}
```

## 5. (Beta) C Style

```c
int64_t CcReferenceSharedCacheMapByVacb(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m28;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (64);
    result = 0;
    v_stack_m18 = 0;
    v_stack_m28 = v_xmm0;
    local_rdi = 0;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x218)) + (768);
    result = KeAcquireInStackQueuedSpinLockAtDpcLevel(Arg1, v_stack_m28, a3, a4);
    result = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x60)) & (-16);
    result = *(uint64_t *)(result + 0x28);
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x28) + 0x8)) == (*(uint64_t *)(arg1 + 0x8))) {
        result = *(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x4);
        local_rdi = 1;
        result = (uint32_t)((result) + 1);
        *(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x4) = (uint32_t)(result);
    }
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(v_stack_m28, v_stack_m28, a3, a4);
    local_rsp = (local_rsp) + (64);
    return (uint8_t)(local_rdi);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0026FCBC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0026FCBC[BB_0026FCBC]
  bb_0026FD0D[BB_0026FD0D]
  bb_0026FD20[BB_0026FD20]
  bb_0026FD38[BB_0026FD38]
  bb_0026FCBC -->|branch| bb_0026FD20
  bb_0026FCBC -->|fallthrough| bb_0026FD0D
  bb_0026FD0D -->|flow| bb_0026FD20
```

# IovUtilGetUpperDeviceObjectWithTag

- RVA: `0x00BA2AE0`–`0x00BA2B2C` (길이 `76` bytes)
- VA: `0x0000000140BA2AE0`
- 실행 섹션: `PAGEVRFY`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `22`개 명령, `76/76` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00BA2AF2` → [KeAcquireQueuedSpinLock](../../text/27/KeAcquireQueuedSpinLock_function_00273D80.md) (function, `0x00273D80`)
- `0x00BA2B0B` → [ObfReferenceObjectWithTag](../../text/21/ObfReferenceObjectWithTag_function_00210710.md) (function, `0x00210710`)
- `0x00BA2B18` → [KeReleaseQueuedSpinLock](../../text/27/KeReleaseQueuedSpinLock_function_00272540.md) (function, `0x00272540`)

### Direct callers
- [IovpExamineDevObjForwarding](../B9/IovpExamineDevObjForwarding_function_00B9D59C.md) at `0x00B9D5AF`
- [IovpExamineDevObjForwarding](../B9/IovpExamineDevObjForwarding_function_00B9D59C.md) at `0x00B9D602`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00BA2AF2` → [KeAcquireQueuedSpinLock](../../text/27/KeAcquireQueuedSpinLock_function_00273D80.md) (`PAGEVRFY` → `.text`)
  - `0x00BA2B0B` → [ObfReferenceObjectWithTag](../../text/21/ObfReferenceObjectWithTag_function_00210710.md) (`PAGEVRFY` → `.text`)
  - `0x00BA2B18` → [KeReleaseQueuedSpinLock](../../text/27/KeReleaseQueuedSpinLock_function_00272540.md) (`PAGEVRFY` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BA2AE0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00BA2AE5  57                              push rdi
00BA2AE6  48 83 EC 20                     sub rsp, 0x20
00BA2AEA  48 8B D9                        mov rbx, rcx
00BA2AED  B9 0A 00 00 00                  mov ecx, 0xa
00BA2AF2  E8 89 12 6D FF                  call 0x140273d80
00BA2AF7  48 8B 5B 18                     mov rbx, qword ptr [rbx + 0x18]
00BA2AFB  40 8A F8                        mov dil, al
00BA2AFE  48 85 DB                        test rbx, rbx
00BA2B01  74 0D                           je 0x140ba2b10
00BA2B03  BA 56 72 66 49                  mov edx, 0x49667256
00BA2B08  48 8B CB                        mov rcx, rbx
00BA2B0B  E8 00 DC 66 FF                  call 0x140210710
00BA2B10  40 8A D7                        mov dl, dil
00BA2B13  B9 0A 00 00 00                  mov ecx, 0xa
00BA2B18  E8 23 FA 6C FF                  call 0x140272540
00BA2B1D  48 8B C3                        mov rax, rbx
00BA2B20  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00BA2B25  48 83 C4 20                     add rsp, 0x20
00BA2B29  5F                              pop rdi
00BA2B2A  C3                              ret
00BA2B2B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IovUtilGetUpperDeviceObjectWithTag(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    result = KeAcquireQueuedSpinLock(10, a2, a3, a4);
    if (*(unsigned __int64 *)(a1 + 24) != 0) {
        a2 = 0x49667256ULL;
        a1 = *(unsigned __int64 *)(a1 + 24);
        result = ObfReferenceObjectWithTag(a1, a2, a3, a4);
    }
    result = KeReleaseQueuedSpinLock(10, (unsigned __int8)((unsigned __int8)(result)), a3, a4);
    v_rsp = (v_rsp) + (32);
    return *(unsigned __int64 *)(a1 + 24);
}
```

## 5. (Beta) C Style

```c
int64_t IovUtilGetUpperDeviceObjectWithTag(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    result = KeAcquireQueuedSpinLock(10, a2, a3, a4);
    if (*(uint64_t *)(arg1 + 0x18) != 0) {
        a2 = 0x49667256ULL;
        Arg1 = *(uint64_t *)(arg1 + 0x18);
        result = ObfReferenceObjectWithTag(Arg1, a2, a3, a4);
    }
    result = KeReleaseQueuedSpinLock(10, (uint8_t)((uint8_t)(result)), a3, a4);
    local_rsp = (local_rsp) + (32);
    return *(uint64_t *)(arg1 + 0x18);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x18` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00BA2AE0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BA2AE0[BB_00BA2AE0]
  bb_00BA2B03[BB_00BA2B03]
  bb_00BA2B10[BB_00BA2B10]
  bb_00BA2B2B[BB_00BA2B2B]
  bb_00BA2AE0 -->|branch| bb_00BA2B10
  bb_00BA2AE0 -->|fallthrough| bb_00BA2B03
  bb_00BA2B03 -->|flow| bb_00BA2B10
```

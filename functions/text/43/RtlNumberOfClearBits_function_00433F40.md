# RtlNumberOfClearBits

- RVA: `0x00433F40`–`0x00433F5B` (길이 `27` bytes)
- VA: `0x0000000140433F40`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `11`개 명령, `27/27` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00433F49` → [RtlNumberOfSetBits](RtlNumberOfSetBits_function_00433F70.md) (function, `0x00433F70`)

### Direct callers
- [PopGetRemainingHibernateRangeDataSize](../../pagelk/B6/PopGetRemainingHibernateRangeDataSize_function_00B6D7A0.md) at `0x00B6D816`
- [PopSaveHiberContext](../../pagelk/B6/PopSaveHiberContext_function_00B6F050.md) at `0x00B6F6D8`
- [PopSaveHiberContext](../../pagelk/B6/PopSaveHiberContext_function_00B6F050.md) at `0x00B6F902`
- [VfThunkApplyThunksCurrentSession](../../pagevrfy/BA/VfThunkApplyThunksCurrentSession_function_00BA719C.md) at `0x00BA7228`
- [VfThunkApplyThunksCurrentSession](../../pagevrfy/BA/VfThunkApplyThunksCurrentSession_function_00BA719C.md) at `0x00BA724B`
- [VfThunkApplyThunksCurrentSession](../../pagevrfy/BA/VfThunkApplyThunksCurrentSession_function_00BA719C.md) at `0x00BA7266`
- [ViThunkFindAllSharedExports](../../pagevrfy/BA/ViThunkFindAllSharedExports_function_00BA755C.md) at `0x00BA757F`
- [ViThunkFindAllSharedExports](../../pagevrfy/BA/ViThunkFindAllSharedExports_function_00BA755C.md) at `0x00BA759C`
- [ViThunkFindAllSharedExports](../../pagevrfy/BA/ViThunkFindAllSharedExports_function_00BA755C.md) at `0x00BA75B9`
- [ViThunkCreateSharedExportInformation](../../pagevrfy/BB/ViThunkCreateSharedExportInformation_function_00BB637C.md) at `0x00BB63A5`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00433F40  40 53                           push rbx
00433F42  48 83 EC 20                     sub rsp, 0x20
00433F46  48 8B D9                        mov rbx, rcx
00433F49  E8 22 00 00 00                  call 0x140433f70
00433F4E  8B 0B                           mov ecx, dword ptr [rbx]
00433F50  2B C8                           sub ecx, eax
00433F52  8B C1                           mov eax, ecx
00433F54  48 83 C4 20                     add rsp, 0x20
00433F58  5B                              pop rbx
00433F59  C3                              ret
00433F5A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlNumberOfClearBits(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = RtlNumberOfSetBits(a1, a2, a3, a4);
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1))) - ((unsigned int)(result)));
    v_rsp = (v_rsp) + (32);
    return (unsigned int)((unsigned int)(a1));
}
```

## 5. (Beta) C Style

```c
int64_t RtlNumberOfClearBits(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = RtlNumberOfSetBits(Arg1, a2, a3, a4);
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1))) - ((uint32_t)(result)));
    local_rsp = (local_rsp) + (32);
    return (uint32_t)((uint32_t)(Arg1));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00433F40&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00433F40[BB_00433F40]
  bb_00433F5A[BB_00433F5A]
```

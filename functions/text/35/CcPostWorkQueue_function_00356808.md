# CcPostWorkQueue

- RVA: `0x00356808`–`0x0035682E` (길이 `38` bytes)
- VA: `0x0000000140356808`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CEE8`
- 디코드: `11`개 명령, `38/38` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **7**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0035681C` → [CcPostWorkQueueRegular](CcPostWorkQueueRegular_function_00356834.md) (function, `0x00356834`)
- `0x00356827` → [CcPostWorkQueueCachemapUninit](CcPostWorkQueueCachemapUninit_function_00356C94.md) (function, `0x00356C94`)

### Direct callers
- [CcRepostToSynchronousLazywriter](CcRepostToSynchronousLazywriter_function_0035492C.md) at `0x003549A5`
- [CcScheduleReadAheadNuma](../38/CcScheduleReadAheadNuma_function_0038883C.md) at `0x00388B74`
- [CcLazyWriteScanVolume](../38/CcLazyWriteScanVolume_function_00388DC0.md) at `0x0038911B`
- [CcLazyWriteScanVolume](../38/CcLazyWriteScanVolume_function_00388DC0.md) at `0x00389505`
- [CcLazyWriteScan](../3C/CcLazyWriteScan_function_003C9394.md) at `0x003C98BC`
- [CcLazyWriteScan](../3C/CcLazyWriteScan_function_003C9394.md) at `0x003C99F8`
- [CcQueueLazyWriteScanThreadForVolume](../3C/CcQueueLazyWriteScanThreadForVolume_function_003C9AF0.md) at `0x003C9CC2`
- [CcQueueLazyWriteScanThread](../57/CcQueueLazyWriteScanThread_function_0057BBD0.md) at `0x0057BE22`
- [sub_006EC29A](../6E/Unknown_function_006EC29A.md) at `0x006EC340`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00356808  48 83 EC 28                     sub rsp, 0x28
0035680C  48 8B 81 98 00 00 00            mov rax, qword ptr [rcx + 0x98]
00356813  48 83 C0 78                     add rax, 0x78
00356817  48 3B C2                        cmp rax, rdx
0035681A  74 0B                           je 0x140356827
0035681C  E8 13 00 00 00                  call 0x140356834
00356821  48 83 C4 28                     add rsp, 0x28
00356825  C3                              ret
00356826  CC                              int3
00356827  E8 68 04 00 00                  call 0x140356c94
0035682C  EB F3                           jmp 0x140356821
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CcPostWorkQueue(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = (*(unsigned __int64 *)(a1 + 152)) + (120);
    if (result == a2) goto loc_00356827;
    result = CcPostWorkQueueRegular(a1, a2, a3, a4);
loc_00356821:
    v_rsp = (v_rsp) + (40);
    return result;
loc_00356827:
    result = CcPostWorkQueueCachemapUninit(a1, a2, a3, a4);
    goto loc_00356821;
}
```

## 5. (Beta) C Style

```c
int64_t CcPostWorkQueue(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = (*(uint64_t *)(arg1 + 0x98)) + (120);
    if (result == Arg2) goto loc_00356827;
    result = CcPostWorkQueueRegular(Arg1, Arg2, a3, a4);
loc_00356821:
    local_rsp = (local_rsp) + (40);
    return result;
loc_00356827:
    result = CcPostWorkQueueCachemapUninit(Arg1, Arg2, a3, a4);
    goto loc_00356821;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x98` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00356808&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00356808[BB_00356808]
  bb_0035681C[BB_0035681C]
  bb_00356821[BB_00356821]
  bb_00356826[BB_00356826]
  bb_00356827[BB_00356827]
  bb_00356808 -->|branch| bb_00356827
  bb_00356808 -->|fallthrough| bb_0035681C
  bb_0035681C -->|flow| bb_00356821
  bb_00356826 -->|flow| bb_00356827
  bb_00356827 -->|branch| bb_00356821
```

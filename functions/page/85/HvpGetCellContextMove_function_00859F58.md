# HvpGetCellContextMove

- RVA: `0x00859F58`–`0x00859F7E` (길이 `38` bytes)
- VA: `0x0000000140859F58`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `12`개 명령, `38/38` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00859F6B` → [HvpGetBinContextMove](HvpGetBinContextMove_function_00859F84.md) (function, `0x00859F84`)
- `0x00859F73` → [HvpGetCellContextReinitialize](HvpGetCellContextReinitialize_function_00855D40.md) (function, `0x00855D40`)

### Direct callers
- [CmpRemoveSubKeyFromList](../84/CmpRemoveSubKeyFromList_function_0084A030.md) at `0x0084A27C`
- [HvAllocateCell](HvAllocateCell_function_00859C94.md) at `0x00859DE0`
- [sub_00859FB9](Unknown_function_00859FB9.md) at `0x0085A0FB`
- [HvReallocateCell](HvReallocateCell_function_0085B5D0.md) at `0x0085B65D`
- [HvReallocateCell](HvReallocateCell_function_0085B5D0.md) at `0x0085B726`
- [CmpMarkIndexDirtyInStorageType](../A3/CmpMarkIndexDirtyInStorageType_function_00A325B0.md) at `0x00A3265A`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00859F58  48 83 EC 28                     sub rsp, 0x28
00859F5C  8B 02                           mov eax, dword ptr [rdx]
00859F5E  4C 8B C2                        mov r8, rdx
00859F61  89 01                           mov dword ptr [rcx], eax
00859F63  48 83 C2 04                     add rdx, 4
00859F67  48 83 C1 04                     add rcx, 4
00859F6B  E8 14 00 00 00                  call 0x140859f84
00859F70  49 8B C8                        mov rcx, r8
00859F73  E8 C8 BD FF FF                  call 0x140855d40
00859F78  48 83 C4 28                     add rsp, 0x28
00859F7C  C3                              ret
00859F7D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HvpGetCellContextMove(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    *(unsigned int *)(a1) = (unsigned int)((unsigned int)(*(unsigned int *)(a2)));
    a2 = (a2) + (4);
    a1 = (a1) + (4);
    result = HvpGetBinContextMove(a1, a2, a2, a4);
    result = HvpGetCellContextReinitialize(a2, a2, a2, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HvpGetCellContextMove(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    *(uint32_t *)(arg1) = (uint32_t)((uint32_t)(*(uint32_t *)(arg2)));
    Arg2 = (Arg2) + (4);
    Arg1 = (Arg1) + (4);
    result = HvpGetBinContextMove(Arg1, Arg2, Arg2, a4);
    result = HvpGetCellContextReinitialize(Arg2, Arg2, Arg2, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `W` |
| `Arg2` | `+ 0x0` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00859F58&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00859F58[BB_00859F58]
  bb_00859F7D[BB_00859F7D]
```

# ExDestroyHandleTable

- RVA: `0x00904D18`–`0x00904D35` (길이 `29` bytes)
- VA: `0x0000000140904D18`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `10`개 명령, `29/29` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00904D21` → [ExpRemoveHandleTable](ExpRemoveHandleTable_function_00903A90.md) (function, `0x00903A90`)
- `0x00904D29` → [ExpFreeHandleTable](ExpFreeHandleTable_function_00903B70.md) (function, `0x00903B70`)

### Direct callers
- [AlpcpAllocateMessageFromExtendedTables](../74/AlpcpAllocateMessageFromExtendedTables_function_0074C500.md) at `0x0074C5AF`
- [ObKillProcess](ObKillProcess_function_00904F30.md) at `0x00904F77`
- [ObInitProcess](../94/ObInitProcess_function_0094C62C.md) at `0x0094C75A`
- [RtlDestroyAtomTable](../9C/RtlDestroyAtomTable_function_009C43F0.md) at `0x009C4475`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00904D18  40 53                           push rbx
00904D1A  48 83 EC 20                     sub rsp, 0x20
00904D1E  48 8B D9                        mov rbx, rcx
00904D21  E8 6A ED FF FF                  call 0x140903a90
00904D26  48 8B CB                        mov rcx, rbx
00904D29  E8 42 EE FF FF                  call 0x140903b70
00904D2E  48 83 C4 20                     add rsp, 0x20
00904D32  5B                              pop rbx
00904D33  C3                              ret
00904D34  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExDestroyHandleTable(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = ExpRemoveHandleTable(a1, a2, a3, a4);
    result = ExpFreeHandleTable(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ExDestroyHandleTable(int64_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = ExpRemoveHandleTable(Arg1, a2, a3, a4);
    result = ExpFreeHandleTable(Arg1, a2, a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00904D18&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00904D18[BB_00904D18]
  bb_00904D34[BB_00904D34]
```

# PpmPdcNotifyMediaBufferingUpdate

- RVA: `0x00A6F0B8`–`0x00A6F0D3` (길이 `27` bytes)
- VA: `0x0000000140A6F0B8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `8`개 명령, `27/27` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00A6F0C8` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [PpmMediaBufferingWorker](../../text/2D/PpmMediaBufferingWorker_function_002DA680.md) at `0x002DA6F8`

### Static image references
- `0x00A6F0BC` → RVA `0x00E677B8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00A6F0C8` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A6F0B8  48 83 EC 28                     sub rsp, 0x28
00A6F0BC  48 8B 05 F5 86 3F 00            mov rax, qword ptr [rip + 0x3f86f5]
00A6F0C3  48 85 C0                        test rax, rax
00A6F0C6  74 05                           je 0x140a6f0cd
00A6F0C8  E8 03 BA C4 FF                  call 0x1406baad0
00A6F0CD  48 83 C4 28                     add rsp, 0x28
00A6F0D1  C3                              ret
00A6F0D2  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PpmPdcNotifyMediaBufferingUpdate(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = *(unsigned __int64 *)(v_rip + 4163317);
    if (*(unsigned __int64 *)(v_rip + 4163317) != 0) {
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void PpmPdcNotifyMediaBufferingUpdate(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = *(uint64_t *)(v_rip + 0x3F86F5);
    if (*(uint64_t *)(v_rip + 0x3F86F5) != 0) {
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A6F0B8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A6F0B8[BB_00A6F0B8]
  bb_00A6F0C8[BB_00A6F0C8]
  bb_00A6F0CD[BB_00A6F0CD]
  bb_00A6F0D2[BB_00A6F0D2]
  bb_00A6F0B8 -->|branch| bb_00A6F0CD
  bb_00A6F0B8 -->|fallthrough| bb_00A6F0C8
  bb_00A6F0C8 -->|flow| bb_00A6F0CD
```

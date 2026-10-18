# FsRtlReleaseFileNameInformation

- RVA: `0x0097DB90`–`0x0097DBAA` (길이 `26` bytes)
- VA: `0x000000014097DB90`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `7`개 명령, `26/26` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **6**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0097DB9F` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [EtwpTraceImageUnloadApc](../../text/44/EtwpTraceImageUnloadApc_function_0044BF50.md) at `0x0044BFF9`
- [EtwpCancelTraceImageUnloadApc](../../text/65/EtwpCancelTraceImageUnloadApc_function_00650810.md) at `0x0065089E`
- [EtwpCovSampModuleNameInfoCleanup](EtwpCovSampModuleNameInfoCleanup_function_0097D96C.md) at `0x0097D99D`
- [EtwpCovSampEnumerateProcess](EtwpCovSampEnumerateProcess_function_0097D9B0.md) at `0x0097DAE3`
- [EtwpCovSampEnumerateProcess](EtwpCovSampEnumerateProcess_function_0097D9B0.md) at `0x0097DB74`
- [PerfLogImageUnload](../A2/PerfLogImageUnload_function_00A2216C.md) at `0x00A223D8`
- [EtwpCovSampModuleGetName](../A5/EtwpCovSampModuleGetName_function_00A5095C.md) at `0x00A50A5F`

### Static image references
- `0x0097DB94` → RVA `0x00E65BF0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0097DB9F` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0097DB90  48 83 EC 28                     sub rsp, 0x28
0097DB94  48 8B 05 55 80 4E 00            mov rax, qword ptr [rip + 0x4e8055]
0097DB9B  48 8B 40 20                     mov rax, qword ptr [rax + 0x20]
0097DB9F  E8 2C CF D3 FF                  call 0x1406baad0
0097DBA4  48 83 C4 28                     add rsp, 0x28
0097DBA8  C3                              ret
0097DBA9  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall FsRtlReleaseFileNameInformation(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = guard_dispatch_icall(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void FsRtlReleaseFileNameInformation(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = guard_dispatch_icall(a1, a2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0097DB90&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0097DB90[BB_0097DB90]
  bb_0097DBA9[BB_0097DBA9]
```

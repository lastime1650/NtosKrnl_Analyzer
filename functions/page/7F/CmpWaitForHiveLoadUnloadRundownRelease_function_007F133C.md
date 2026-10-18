# CmpWaitForHiveLoadUnloadRundownRelease

- RVA: `0x007F133C`–`0x007F135E` (길이 `34` bytes)
- VA: `0x00000001407F133C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `8`개 명령, `34/34` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x007F1347` → [ExWaitForRundownProtectionRelease](../../text/2A/ExWaitForRundownProtectionRelease_function_002A4CB0.md) (function, `0x002A4CB0`)

### Direct callers
- [CmShutdownSystem1](../../text/66/CmShutdownSystem1_function_0066A5B0.md) at `0x0066A5E5`

### Static image references
- `0x007F1340` → RVA `0x00EF7B28` (`.data`; read)
- `0x007F1351` → RVA `0x00EF7B28` (`.data`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x007F1347` → [ExWaitForRundownProtectionRelease](../../text/2A/ExWaitForRundownProtectionRelease_function_002A4CB0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007F133C  48 83 EC 28                     sub rsp, 0x28
007F1340  48 8D 0D E1 67 70 00            lea rcx, [rip + 0x7067e1]
007F1347  E8 64 39 AB FF                  call 0x1402a4cb0
007F134C  B8 01 00 00 00                  mov eax, 1
007F1351  48 87 05 D0 67 70 00            xchg qword ptr [rip + 0x7067d0], rax
007F1358  48 83 C4 28                     add rsp, 0x28
007F135C  C3                              ret
007F135D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpWaitForHiveLoadUnloadRundownRelease(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = ExWaitForRundownProtectionRelease(v_rip + 7366625, a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return 1;
}
```

## 5. (Beta) C Style

```c
void CmpWaitForHiveLoadUnloadRundownRelease(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = ExWaitForRundownProtectionRelease(v_rip + 7366625, a2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return 1;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007F133C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007F133C[BB_007F133C]
  bb_007F135D[BB_007F135D]
```

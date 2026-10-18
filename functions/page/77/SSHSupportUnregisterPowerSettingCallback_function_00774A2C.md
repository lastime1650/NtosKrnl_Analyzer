# SSHSupportUnregisterPowerSettingCallback

- RVA: `0x00774A2C`–`0x00774A42` (길이 `22` bytes)
- VA: `0x0000000140774A2C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `6`개 명령, `22/22` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00774A37` → [PoUnregisterPowerSettingCallback](../A8/PoUnregisterPowerSettingCallback_function_00A8E940.md) (function, `0x00A8E940`)

### Direct callers
- [SshpUninitialize](../../init/C4/SshpUninitialize_function_00C44798.md) at `0x00C447A5`

### Static image references
- `0x00774A30` → RVA `0x00F06B58` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00774A2C  48 83 EC 28                     sub rsp, 0x28
00774A30  48 8B 0D 21 21 79 00            mov rcx, qword ptr [rip + 0x792121]
00774A37  E8 04 9F 31 00                  call 0x140a8e940
00774A3C  48 83 C4 28                     add rsp, 0x28
00774A40  C3                              ret
00774A41  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SSHSupportUnregisterPowerSettingCallback(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = PoUnregisterPowerSettingCallback(*(unsigned __int64 *)(v_rip + 7938337), a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void SSHSupportUnregisterPowerSettingCallback(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = PoUnregisterPowerSettingCallback(*(uint64_t *)(v_rip + 0x792121), a2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00774A2C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00774A2C[BB_00774A2C]
  bb_00774A41[BB_00774A41]
```

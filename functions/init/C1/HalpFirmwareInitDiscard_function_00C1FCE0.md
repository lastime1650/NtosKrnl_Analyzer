# HalpFirmwareInitDiscard

- RVA: `0x00C1FCE0`–`0x00C1FD27` (길이 `71` bytes)
- VA: `0x0000000140C1FCE0`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `13`개 명령, `71/71` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **8**

### Outgoing calls
- `0x00C1FD1C` → [HalpEfiInitialization](HalpEfiInitialization_function_00C1F644.md) (function, `0x00C1F644`)

### Direct callers
- [HalpFirmwareInitSystem](../../pagelk/B5/HalpFirmwareInitSystem_function_00B5D4F0.md) at `0x00B5D4FC`

### Static image references
- `0x00C1FCE4` → RVA `0x00563CE0` (`HalpQueryCapsuleCapabilities`; read)
- `0x00C1FCEB` → RVA `0x00E00AA0` (`.data`; write)
- `0x00C1FCF2` → RVA `0x00563E30` (`HalpUpdateCapsule`; read)
- `0x00C1FCF9` → RVA `0x00E00AA8` (`.data`; write)
- `0x00C1FD00` → RVA `0x0054E190` (`HalpIsEFIRuntimeActive`; read)
- `0x00C1FD07` → RVA `0x00E00BA0` (`.data`; write)
- `0x00C1FD0E` → RVA `0x004492D0` (`HalpEnumerateEnvironmentVariablesWithFilter`; read)
- `0x00C1FD15` → RVA `0x00E00BE0` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C1FCE0  48 83 EC 28                     sub rsp, 0x28
00C1FCE4  48 8D 05 F5 3F 94 FF            lea rax, [rip - 0x6bc00b]
00C1FCEB  48 89 05 AE 0D 1E 00            mov qword ptr [rip + 0x1e0dae], rax
00C1FCF2  48 8D 05 37 41 94 FF            lea rax, [rip - 0x6bbec9]
00C1FCF9  48 89 05 A8 0D 1E 00            mov qword ptr [rip + 0x1e0da8], rax
00C1FD00  48 8D 05 89 E4 92 FF            lea rax, [rip - 0x6d1b77]
00C1FD07  48 89 05 92 0E 1E 00            mov qword ptr [rip + 0x1e0e92], rax
00C1FD0E  48 8D 05 BB 95 82 FF            lea rax, [rip - 0x7d6a45]
00C1FD15  48 89 05 C4 0E 1E 00            mov qword ptr [rip + 0x1e0ec4], rax
00C1FD1C  E8 23 F9 FF FF                  call 0x140c1f644
00C1FD21  48 83 C4 28                     add rsp, 0x28
00C1FD25  C3                              ret
00C1FD26  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpFirmwareInitDiscard(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    *(unsigned __int64 *)(v_rip + 1969582) = v_rip - 7061515;
    *(unsigned __int64 *)(v_rip + 1969576) = v_rip - 7061193;
    *(unsigned __int64 *)(v_rip + 1969810) = v_rip - 7150455;
    *(unsigned __int64 *)(v_rip + 1969860) = v_rip - 8219205;
    result = HalpEfiInitialization(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void HalpFirmwareInitDiscard(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    *(uint64_t *)(v_rip + 0x1E0DAE) = v_rip - 7061515;
    *(uint64_t *)(v_rip + 0x1E0DA8) = v_rip - 7061193;
    *(uint64_t *)(v_rip + 0x1E0E92) = v_rip - 7150455;
    *(uint64_t *)(v_rip + 0x1E0EC4) = v_rip - 8219205;
    result = HalpEfiInitialization(a1, a2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C1FCE0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00C1FCE0[BB_00C1FCE0]
  bb_00C1FD26[BB_00C1FD26]
```

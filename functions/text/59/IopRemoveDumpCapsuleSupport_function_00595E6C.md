# IopRemoveDumpCapsuleSupport

- RVA: `0x00595E6C`–`0x00595EA3` (길이 `55` bytes)
- VA: `0x0000000140595E6C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `14`개 명령, `55/55` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x00595E87` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [IoConfigureCrashDump](IoConfigureCrashDump_function_00591CB4.md) at `0x00591DF9`
- [IoConfigureCrashDump](IoConfigureCrashDump_function_00591CB4.md) at `0x00591E4B`
- [IoInitializeCrashDump](../../page/71/IoInitializeCrashDump_function_00719D88.md) at `0x00719DEB`
- [IoInitSystemPreDrivers](../../init/C2/IoInitSystemPreDrivers_function_00C2AC3C.md) at `0x00C2BCFC`

### Static image references
- `0x00595E70` → RVA `0x00E65F60` (`.data`; read)
- `0x00595E79` → RVA `0x00E65F58` (`.data`; read)
- `0x00595E8C` → RVA `0x00E65F58` (`.data`; read/write)
- `0x00595E94` → RVA `0x00E65F60` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00595E87` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00595E6C  48 83 EC 28                     sub rsp, 0x28
00595E70  80 3D E9 00 8D 00 01            cmp byte ptr [rip + 0x8d00e9], 1
00595E77  75 22                           jne 0x140595e9b
00595E79  48 8B 0D D8 00 8D 00            mov rcx, qword ptr [rip + 0x8d00d8]
00595E80  48 85 C9                        test rcx, rcx
00595E83  74 0F                           je 0x140595e94
00595E85  33 D2                           xor edx, edx
00595E87  E8 E4 C9 5E 00                  call 0x140b82870
00595E8C  48 83 25 C4 00 8D 00 00         and qword ptr [rip + 0x8d00c4], 0
00595E94  C6 05 C5 00 8D 00 00            mov byte ptr [rip + 0x8d00c5], 0
00595E9B  33 C0                           xor eax, eax
00595E9D  48 83 C4 28                     add rsp, 0x28
00595EA1  C3                              ret
00595EA2  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IopRemoveDumpCapsuleSupport(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if ((*(unsigned __int8 *)(v_rip + 9240809)) != 1) goto loc_00595E9B;
    if (*(unsigned __int64 *)(v_rip + 9240792) != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(v_rip + 9240792), a2, a3, a4);
    }
    *(unsigned __int8 *)(v_rip + 9240773) = 0;
loc_00595E9B:
    result = 0;
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t IopRemoveDumpCapsuleSupport(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if ((*(uint8_t *)(v_rip + 0x8D00E9)) != 1) goto loc_00595E9B;
    if (*(uint64_t *)(v_rip + 0x8D00D8) != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(v_rip + 0x8D00D8), Arg2, a3, a4);
    }
    *(uint8_t *)(v_rip + 0x8D00C5) = 0;
loc_00595E9B:
    result = 0;
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00595E6C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00595E6C[BB_00595E6C]
  bb_00595E79[BB_00595E79]
  bb_00595E85[BB_00595E85]
  bb_00595E94[BB_00595E94]
  bb_00595E9B[BB_00595E9B]
  bb_00595EA2[BB_00595EA2]
  bb_00595E6C -->|branch| bb_00595E9B
  bb_00595E6C -->|fallthrough| bb_00595E79
  bb_00595E79 -->|branch| bb_00595E94
  bb_00595E79 -->|fallthrough| bb_00595E85
  bb_00595E85 -->|flow| bb_00595E94
  bb_00595E94 -->|flow| bb_00595E9B
```

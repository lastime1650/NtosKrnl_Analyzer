# CcResetGlobalTelemetry

- RVA: `0x00ACF980`–`0x00ACF9FB` (길이 `123` bytes)
- VA: `0x0000000140ACF980`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `20`개 명령, `123/123` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **17**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [CcPostVolumeTelemetry](../../text/42/CcPostVolumeTelemetry_function_00420FF8.md) at `0x004212E8`

### Static image references
- `0x00ACF982` → RVA `0x00F8F2B0` (`.data`; write)
- `0x00ACF989` → RVA `0x00F8F2B8` (`.data`; write)
- `0x00ACF990` → RVA `0x00F8F2C0` (`.data`; write)
- `0x00ACF997` → RVA `0x00F8F2C8` (`.data`; write)
- `0x00ACF99E` → RVA `0x00F8F2D0` (`.data`; write)
- `0x00ACF9A5` → RVA `0x00F8F2D8` (`.data`; write)
- `0x00ACF9AC` → RVA `0x00F8F2E0` (`.data`; write)
- `0x00ACF9B3` → RVA `0x00F8F2E8` (`.data`; write)
- `0x00ACF9BA` → RVA `0x00F8F2F0` (`.data`; write)
- `0x00ACF9C1` → RVA `0x00F8F2F8` (`.data`; write)
- `0x00ACF9C8` → RVA `0x00F8F300` (`.data`; write)
- `0x00ACF9CF` → RVA `0x00F8F308` (`.data`; write)
- `0x00ACF9D6` → RVA `0x00F8F310` (`.data`; write)
- `0x00ACF9DD` → RVA `0x00F8F318` (`.data`; write)
- `0x00ACF9E4` → RVA `0x00F8F320` (`.data`; write)
- `0x00ACF9EB` → RVA `0x00F8F328` (`.data`; write)
- `0x00ACF9F2` → RVA `0x00F8F330` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00ACF980  33 C0                           xor eax, eax
00ACF982  48 89 05 27 F9 4B 00            mov qword ptr [rip + 0x4bf927], rax
00ACF989  48 89 05 28 F9 4B 00            mov qword ptr [rip + 0x4bf928], rax
00ACF990  48 89 05 29 F9 4B 00            mov qword ptr [rip + 0x4bf929], rax
00ACF997  48 89 05 2A F9 4B 00            mov qword ptr [rip + 0x4bf92a], rax
00ACF99E  48 89 05 2B F9 4B 00            mov qword ptr [rip + 0x4bf92b], rax
00ACF9A5  48 89 05 2C F9 4B 00            mov qword ptr [rip + 0x4bf92c], rax
00ACF9AC  48 89 05 2D F9 4B 00            mov qword ptr [rip + 0x4bf92d], rax
00ACF9B3  48 89 05 2E F9 4B 00            mov qword ptr [rip + 0x4bf92e], rax
00ACF9BA  48 89 05 2F F9 4B 00            mov qword ptr [rip + 0x4bf92f], rax
00ACF9C1  48 89 05 30 F9 4B 00            mov qword ptr [rip + 0x4bf930], rax
00ACF9C8  48 89 05 31 F9 4B 00            mov qword ptr [rip + 0x4bf931], rax
00ACF9CF  48 89 05 32 F9 4B 00            mov qword ptr [rip + 0x4bf932], rax
00ACF9D6  48 89 05 33 F9 4B 00            mov qword ptr [rip + 0x4bf933], rax
00ACF9DD  48 89 05 34 F9 4B 00            mov qword ptr [rip + 0x4bf934], rax
00ACF9E4  48 89 05 35 F9 4B 00            mov qword ptr [rip + 0x4bf935], rax
00ACF9EB  48 89 05 36 F9 4B 00            mov qword ptr [rip + 0x4bf936], rax
00ACF9F2  48 89 05 37 F9 4B 00            mov qword ptr [rip + 0x4bf937], rax
00ACF9F9  C3                              ret
00ACF9FA  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CcResetGlobalTelemetry(void)
{
    __int64 result;

    result = 0;
    *(unsigned __int64 *)(v_rip + 4978983) = 0;
    *(unsigned __int64 *)(v_rip + 4978984) = 0;
    *(unsigned __int64 *)(v_rip + 4978985) = 0;
    *(unsigned __int64 *)(v_rip + 4978986) = 0;
    *(unsigned __int64 *)(v_rip + 4978987) = 0;
    *(unsigned __int64 *)(v_rip + 4978988) = 0;
    *(unsigned __int64 *)(v_rip + 4978989) = 0;
    *(unsigned __int64 *)(v_rip + 4978990) = 0;
    *(unsigned __int64 *)(v_rip + 4978991) = 0;
    *(unsigned __int64 *)(v_rip + 4978992) = 0;
    *(unsigned __int64 *)(v_rip + 4978993) = 0;
    *(unsigned __int64 *)(v_rip + 4978994) = 0;
    *(unsigned __int64 *)(v_rip + 4978995) = 0;
    *(unsigned __int64 *)(v_rip + 4978996) = 0;
    *(unsigned __int64 *)(v_rip + 4978997) = 0;
    *(unsigned __int64 *)(v_rip + 4978998) = 0;
    *(unsigned __int64 *)(v_rip + 4978999) = 0;
    return result;
}
```

## 5. (Beta) C Style

```c
void CcResetGlobalTelemetry(void)
{
    int64_t result;

    result = 0;
    *(uint64_t *)(v_rip + 0x4BF927) = 0;
    *(uint64_t *)(v_rip + 0x4BF928) = 0;
    *(uint64_t *)(v_rip + 0x4BF929) = 0;
    *(uint64_t *)(v_rip + 0x4BF92A) = 0;
    *(uint64_t *)(v_rip + 0x4BF92B) = 0;
    *(uint64_t *)(v_rip + 0x4BF92C) = 0;
    *(uint64_t *)(v_rip + 0x4BF92D) = 0;
    *(uint64_t *)(v_rip + 0x4BF92E) = 0;
    *(uint64_t *)(v_rip + 0x4BF92F) = 0;
    *(uint64_t *)(v_rip + 0x4BF930) = 0;
    *(uint64_t *)(v_rip + 0x4BF931) = 0;
    *(uint64_t *)(v_rip + 0x4BF932) = 0;
    *(uint64_t *)(v_rip + 0x4BF933) = 0;
    *(uint64_t *)(v_rip + 0x4BF934) = 0;
    *(uint64_t *)(v_rip + 0x4BF935) = 0;
    *(uint64_t *)(v_rip + 0x4BF936) = 0;
    *(uint64_t *)(v_rip + 0x4BF937) = 0;
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00ACF980&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00ACF980[BB_00ACF980]
  bb_00ACF9FA[BB_00ACF9FA]
```

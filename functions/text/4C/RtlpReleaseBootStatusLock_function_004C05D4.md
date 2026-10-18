# RtlpReleaseBootStatusLock

- RVA: `0x004C05D4`–`0x004C060E` (길이 `58` bytes)
- VA: `0x00000001404C05D4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `14`개 명령, `58/58` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x004C05F2` → [ExfTryToWakePushLock](../26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x004C05FE` → [KeAbPostRelease](../2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x004C0603` → [KeLeaveCriticalRegion](../25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)

### Direct callers
- [PopBootStatGet](../../page/A4/PopBootStatGet_function_00A4C398.md) at `0x00A4C587`
- [PopBootStatSet](../../page/A4/PopBootStatSet_function_00A4C77C.md) at `0x00A4C8A7`
- [RtlUnlockBootStatusData](../../page/A4/RtlUnlockBootStatusData_function_00A4CAF0.md) at `0x00A4CB83`
- [RtlLockBootStatusData](../../page/A9/RtlLockBootStatusData_function_00A94BE0.md) at `0x00A94C44`
- [PopBootStatRestoreDefaults](../../page/AC/PopBootStatRestoreDefaults_function_00AC38E8.md) at `0x00AC3A4C`

### Static image references
- `0x004C05DC` → RVA `0x00E67B10` (`.data`; read/write)
- `0x004C05EB` → RVA `0x00E67B10` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004C05D4  48 83 EC 28                     sub rsp, 0x28
004C05D8  48 83 C8 FF                     or rax, 0xffffffffffffffff
004C05DC  F0 48 0F C1 05 2B 75 9A 00      lock xadd qword ptr [rip + 0x9a752b], rax
004C05E5  24 06                           and al, 6
004C05E7  3C 02                           cmp al, 2
004C05E9  75 0C                           jne 0x1404c05f7
004C05EB  48 8D 0D 1E 75 9A 00            lea rcx, [rip + 0x9a751e]
004C05F2  E8 D9 57 DA FF                  call 0x140265dd0
004C05F7  48 8D 0D 12 75 9A 00            lea rcx, [rip + 0x9a7512]
004C05FE  E8 FD 0F E2 FF                  call 0x1402e1600
004C0603  E8 A8 D2 D9 FF                  call 0x14025d8b0
004C0608  48 83 C4 28                     add rsp, 0x28
004C060C  C3                              ret
004C060D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlpReleaseBootStatusLock(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = (result) | (-1);
    result = (unsigned __int8)((result) & (6));
    if (((unsigned __int8)(result)) == 2) {
        a1 = v_rip + 10122526;
        result = ExfTryToWakePushLock(a1, a2, a3, a4);
    }
    result = KeAbPostRelease(v_rip + 10122514, a2, a3, a4);
    result = KeLeaveCriticalRegion(v_rip + 10122514, a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void RtlpReleaseBootStatusLock(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = (result) | (-1);
    result = (uint8_t)((result) & (6));
    if (((uint8_t)(result)) == 2) {
        a1 = v_rip + 10122526;
        result = ExfTryToWakePushLock(a1, a2, a3, a4);
    }
    result = KeAbPostRelease(v_rip + 10122514, a2, a3, a4);
    result = KeLeaveCriticalRegion(v_rip + 10122514, a2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004C05D4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004C05D4[BB_004C05D4]
  bb_004C05EB[BB_004C05EB]
  bb_004C05F7[BB_004C05F7]
  bb_004C060D[BB_004C060D]
  bb_004C05D4 -->|branch| bb_004C05F7
  bb_004C05D4 -->|fallthrough| bb_004C05EB
  bb_004C05EB -->|flow| bb_004C05F7
```

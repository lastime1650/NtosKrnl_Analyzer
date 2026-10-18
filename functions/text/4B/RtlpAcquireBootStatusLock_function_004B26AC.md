# RtlpAcquireBootStatusLock

- RVA: `0x004B26AC`–`0x004B2709` (길이 `93` bytes)
- VA: `0x00000001404B26AC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `23`개 명령, `93/93` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x004B26CF` → [KeAbPreAcquire](../21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x004B26F4` → [ExfAcquirePushLockExclusiveEx](../20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)

### Direct callers
- [PopBootStatGet](../../page/A4/PopBootStatGet_function_00A4C398.md) at `0x00A4C563`
- [PopBootStatSet](../../page/A4/PopBootStatSet_function_00A4C77C.md) at `0x00A4C883`
- [RtlUnlockBootStatusData](../../page/A4/RtlUnlockBootStatusData_function_00A4CAF0.md) at `0x00A4CB10`
- [RtlLockBootStatusData](../../page/A9/RtlLockBootStatusData_function_00A94BE0.md) at `0x00A94C20`
- [PopBootStatRestoreDefaults](../../page/AC/PopBootStatRestoreDefaults_function_00AC38E8.md) at `0x00AC398C`

### Static image references
- `0x004B26BB` → RVA `0x00E67B10` (`.data`; read)
- `0x004B26D4` → RVA `0x00E67B10` (`.data`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004B26AC  40 53                           push rbx
004B26AE  48 83 EC 20                     sub rsp, 0x20
004B26B2  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
004B26BB  48 8D 0D 4E 54 9B 00            lea rcx, [rip + 0x9b544e]
004B26C2  45 33 C0                        xor r8d, r8d
004B26C5  33 D2                           xor edx, edx
004B26C7  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
004B26CE  90                              nop
004B26CF  E8 5C DB D5 FF                  call 0x140210230
004B26D4  F0 48 0F BA 2D 32 54 9B 00 00   lock bts qword ptr [rip + 0x9b5432], 0
004B26DE  48 8B D8                        mov rbx, rax
004B26E1  73 16                           jae 0x1404b26f9
004B26E3  4C 8D 05 26 54 9B 00            lea r8, [rip + 0x9b5426]
004B26EA  48 8B D0                        mov rdx, rax
004B26ED  48 8D 0D 1C 54 9B 00            lea rcx, [rip + 0x9b541c]
004B26F4  E8 97 D5 D5 FF                  call 0x14020fc90
004B26F9  48 85 DB                        test rbx, rbx
004B26FC  74 04                           je 0x1404b2702
004B26FE  C6 43 0A 01                     mov byte ptr [rbx + 0xa], 1
004B2702  48 83 C4 20                     add rsp, 0x20
004B2706  5B                              pop rbx
004B2707  C3                              ret
004B2708  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlpAcquireBootStatusLock(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_rip + 10179662, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = v_rip + 10179622;
        a2 = result;
        a1 = v_rip + 10179612;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t RtlpAcquireBootStatusLock(int64_t Arg1, int32_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(v_rip + 10179662, Arg2, Arg3, a4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = v_rip + 10179622;
        Arg2 = result;
        Arg1 = v_rip + 10179612;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, a4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004B26AC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004B26AC[BB_004B26AC]
  bb_004B26E3[BB_004B26E3]
  bb_004B26F9[BB_004B26F9]
  bb_004B26FE[BB_004B26FE]
  bb_004B2702[BB_004B2702]
  bb_004B2708[BB_004B2708]
  bb_004B26AC -->|branch| bb_004B26F9
  bb_004B26AC -->|fallthrough| bb_004B26E3
  bb_004B26E3 -->|flow| bb_004B26F9
  bb_004B26F9 -->|branch| bb_004B2702
  bb_004B26F9 -->|fallthrough| bb_004B26FE
  bb_004B26FE -->|flow| bb_004B2702
```

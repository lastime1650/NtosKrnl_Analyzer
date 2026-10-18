# PspAcquirePushLockExclusive

- RVA: `0x005E3FDC`–`0x005E4039` (길이 `93` bytes)
- VA: `0x00000001405E3FDC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `23`개 명령, `93/93` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x005E3FFF` → [KeAbPreAcquire](../21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x005E4024` → [ExfAcquirePushLockExclusiveEx](../20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)

### Direct callers
- [PsStartSiloMonitor](../../page/78/PsStartSiloMonitor_function_007867C0.md) at `0x007867F8`
- [PsUnregisterSiloMonitor](../../page/78/PsUnregisterSiloMonitor_function_00786A00.md) at `0x00786A2E`

### Static image references
- `0x005E3FEB` → RVA `0x00FD9B60` (`PAGEDATA`; read)
- `0x005E4004` → RVA `0x00FD9B60` (`PAGEDATA`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005E3FDC  40 53                           push rbx
005E3FDE  48 83 EC 20                     sub rsp, 0x20
005E3FE2  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
005E3FEB  48 8D 0D 6E 5B 9F 00            lea rcx, [rip + 0x9f5b6e]
005E3FF2  45 33 C0                        xor r8d, r8d
005E3FF5  33 D2                           xor edx, edx
005E3FF7  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
005E3FFE  90                              nop
005E3FFF  E8 2C C2 C2 FF                  call 0x140210230
005E4004  F0 48 0F BA 2D 52 5B 9F 00 00   lock bts qword ptr [rip + 0x9f5b52], 0
005E400E  48 8B D8                        mov rbx, rax
005E4011  73 16                           jae 0x1405e4029
005E4013  4C 8D 05 46 5B 9F 00            lea r8, [rip + 0x9f5b46]
005E401A  48 8B D0                        mov rdx, rax
005E401D  48 8D 0D 3C 5B 9F 00            lea rcx, [rip + 0x9f5b3c]
005E4024  E8 67 BC C2 FF                  call 0x14020fc90
005E4029  48 85 DB                        test rbx, rbx
005E402C  74 04                           je 0x1405e4032
005E402E  C6 43 0A 01                     mov byte ptr [rbx + 0xa], 1
005E4032  48 83 C4 20                     add rsp, 0x20
005E4036  5B                              pop rbx
005E4037  C3                              ret
005E4038  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PspAcquirePushLockExclusive(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_rip + 10443630, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = v_rip + 10443590;
        a2 = result;
        a1 = v_rip + 10443580;
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
int64_t PspAcquirePushLockExclusive(int64_t Arg1, int32_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(v_rip + 10443630, Arg2, Arg3, a4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = v_rip + 10443590;
        Arg2 = result;
        Arg1 = v_rip + 10443580;
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

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005E3FDC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005E3FDC[BB_005E3FDC]
  bb_005E4013[BB_005E4013]
  bb_005E4029[BB_005E4029]
  bb_005E402E[BB_005E402E]
  bb_005E4032[BB_005E4032]
  bb_005E4038[BB_005E4038]
  bb_005E3FDC -->|branch| bb_005E4029
  bb_005E3FDC -->|fallthrough| bb_005E4013
  bb_005E4013 -->|flow| bb_005E4029
  bb_005E4029 -->|branch| bb_005E4032
  bb_005E4029 -->|fallthrough| bb_005E402E
  bb_005E402E -->|flow| bb_005E4032
```

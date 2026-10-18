# PspAcquireSyscallProviderRegistrationLockExclusive

- RVA: `0x005E2284`–`0x005E22E1` (길이 `93` bytes)
- VA: `0x00000001405E2284`
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
- `0x005E22A7` → [KeAbPreAcquire](../21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x005E22CC` → [ExfAcquirePushLockExclusiveEx](../20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)

### Direct callers
- [PsRegisterSyscallProvider](../../page/77/PsRegisterSyscallProvider_function_0077E140.md) at `0x0077E259`
- [PspDestroySyscallProvider](../../page/77/PspDestroySyscallProvider_function_0077E454.md) at `0x0077E45D`

### Static image references
- `0x005E2293` → RVA `0x00FD9BF0` (`PAGEDATA`; read)
- `0x005E22AC` → RVA `0x00FD9BF0` (`PAGEDATA`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005E2284  40 53                           push rbx
005E2286  48 83 EC 20                     sub rsp, 0x20
005E228A  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
005E2293  48 8D 0D 56 79 9F 00            lea rcx, [rip + 0x9f7956]
005E229A  45 33 C0                        xor r8d, r8d
005E229D  33 D2                           xor edx, edx
005E229F  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
005E22A6  90                              nop
005E22A7  E8 84 DF C2 FF                  call 0x140210230
005E22AC  F0 48 0F BA 2D 3A 79 9F 00 00   lock bts qword ptr [rip + 0x9f793a], 0
005E22B6  48 8B D8                        mov rbx, rax
005E22B9  73 16                           jae 0x1405e22d1
005E22BB  4C 8D 05 2E 79 9F 00            lea r8, [rip + 0x9f792e]
005E22C2  48 8B D0                        mov rdx, rax
005E22C5  48 8D 0D 24 79 9F 00            lea rcx, [rip + 0x9f7924]
005E22CC  E8 BF D9 C2 FF                  call 0x14020fc90
005E22D1  48 85 DB                        test rbx, rbx
005E22D4  74 04                           je 0x1405e22da
005E22D6  C6 43 0A 01                     mov byte ptr [rbx + 0xa], 1
005E22DA  48 83 C4 20                     add rsp, 0x20
005E22DE  5B                              pop rbx
005E22DF  C3                              ret
005E22E0  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PspAcquireSyscallProviderRegistrationLockExclusive(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_rip + 10451286, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = v_rip + 10451246;
        a2 = result;
        a1 = v_rip + 10451236;
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
int64_t PspAcquireSyscallProviderRegistrationLockExclusive(int64_t Arg1, int32_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(v_rip + 10451286, Arg2, Arg3, a4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = v_rip + 10451246;
        Arg2 = result;
        Arg1 = v_rip + 10451236;
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

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005E2284&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005E2284[BB_005E2284]
  bb_005E22BB[BB_005E22BB]
  bb_005E22D1[BB_005E22D1]
  bb_005E22D6[BB_005E22D6]
  bb_005E22DA[BB_005E22DA]
  bb_005E22E0[BB_005E22E0]
  bb_005E2284 -->|branch| bb_005E22D1
  bb_005E2284 -->|fallthrough| bb_005E22BB
  bb_005E22BB -->|flow| bb_005E22D1
  bb_005E22D1 -->|branch| bb_005E22DA
  bb_005E22D1 -->|fallthrough| bb_005E22D6
  bb_005E22D6 -->|flow| bb_005E22DA
```

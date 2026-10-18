# CmpLockContextListExclusive

- RVA: `0x00936C7C`–`0x00936CD9` (길이 `93` bytes)
- VA: `0x0000000140936C7C`
- 실행 섹션: `PAGE`
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
- `0x00936C9F` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00936CC4` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)

### Direct callers
- [CmUnRegisterCallback](../7E/CmUnRegisterCallback_function_007E1510.md) at `0x007E168D`
- [CmUnRegisterCallback](../7E/CmUnRegisterCallback_function_007E1510.md) at `0x007E1769`
- [sub_0093691A](Unknown_function_0093691A.md) at `0x00936A7E`

### Static image references
- `0x00936C8B` → RVA `0x00EF7BC8` (`.data`; read)
- `0x00936CA4` → RVA `0x00EF7BC8` (`.data`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00936C9F` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x00936CC4` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00936C7C  40 53                           push rbx
00936C7E  48 83 EC 20                     sub rsp, 0x20
00936C82  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00936C8B  48 8D 0D 36 0F 5C 00            lea rcx, [rip + 0x5c0f36]
00936C92  45 33 C0                        xor r8d, r8d
00936C95  33 D2                           xor edx, edx
00936C97  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00936C9E  90                              nop
00936C9F  E8 8C 95 8D FF                  call 0x140210230
00936CA4  F0 48 0F BA 2D 1A 0F 5C 00 00   lock bts qword ptr [rip + 0x5c0f1a], 0
00936CAE  48 8B D8                        mov rbx, rax
00936CB1  73 16                           jae 0x140936cc9
00936CB3  4C 8D 05 0E 0F 5C 00            lea r8, [rip + 0x5c0f0e]
00936CBA  48 8B D0                        mov rdx, rax
00936CBD  48 8D 0D 04 0F 5C 00            lea rcx, [rip + 0x5c0f04]
00936CC4  E8 C7 8F 8D FF                  call 0x14020fc90
00936CC9  48 85 DB                        test rbx, rbx
00936CCC  74 04                           je 0x140936cd2
00936CCE  C6 43 0A 01                     mov byte ptr [rbx + 0xa], 1
00936CD2  48 83 C4 20                     add rsp, 0x20
00936CD6  5B                              pop rbx
00936CD7  C3                              ret
00936CD8  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpLockContextListExclusive(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_rip + 6033206, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = v_rip + 6033166;
        a2 = result;
        a1 = v_rip + 6033156;
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
int64_t CmpLockContextListExclusive(int64_t Arg1, int32_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(v_rip + 6033206, Arg2, Arg3, a4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = v_rip + 6033166;
        Arg2 = result;
        Arg1 = v_rip + 6033156;
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

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00936C7C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00936C7C[BB_00936C7C]
  bb_00936CB3[BB_00936CB3]
  bb_00936CC9[BB_00936CC9]
  bb_00936CCE[BB_00936CCE]
  bb_00936CD2[BB_00936CD2]
  bb_00936CD8[BB_00936CD8]
  bb_00936C7C -->|branch| bb_00936CC9
  bb_00936C7C -->|fallthrough| bb_00936CB3
  bb_00936CB3 -->|flow| bb_00936CC9
  bb_00936CC9 -->|branch| bb_00936CD2
  bb_00936CC9 -->|fallthrough| bb_00936CCE
  bb_00936CCE -->|flow| bb_00936CD2
```

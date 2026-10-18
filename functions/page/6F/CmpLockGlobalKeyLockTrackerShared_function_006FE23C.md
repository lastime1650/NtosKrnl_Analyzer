# CmpLockGlobalKeyLockTrackerShared

- RVA: `0x006FE23C`–`0x006FE2A1` (길이 `101` bytes)
- VA: `0x00000001406FE23C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `26`개 명령, `101/101` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x006FE25F` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x006FE28C` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)

### Direct callers
- [CmpGlobalLockKeyForWrite](../A7/CmpGlobalLockKeyForWrite_function_00A7CD88.md) at `0x00A7CDA7`

### Static image references
- `0x006FE24B` → RVA `0x00EF5860` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x006FE25F` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x006FE28C` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006FE23C  40 53                           push rbx
006FE23E  48 83 EC 20                     sub rsp, 0x20
006FE242  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
006FE24B  48 8D 0D 0E 76 7F 00            lea rcx, [rip + 0x7f760e]
006FE252  45 33 C0                        xor r8d, r8d
006FE255  33 D2                           xor edx, edx
006FE257  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
006FE25E  90                              nop
006FE25F  E8 CC 1F B1 FF                  call 0x140210230
006FE264  48 8B D8                        mov rbx, rax
006FE267  BA 11 00 00 00                  mov edx, 0x11
006FE26C  33 C0                           xor eax, eax
006FE26E  F0 48 0F B1 15 E9 75 7F 00      lock cmpxchg qword ptr [rip + 0x7f75e9], rdx
006FE277  74 18                           je 0x1406fe291
006FE279  4C 8D 0D E0 75 7F 00            lea r9, [rip + 0x7f75e0]
006FE280  4C 8B C3                        mov r8, rbx
006FE283  33 D2                           xor edx, edx
006FE285  48 8D 0D D4 75 7F 00            lea rcx, [rip + 0x7f75d4]
006FE28C  E8 BB 21 B1 FF                  call 0x14021044c
006FE291  48 85 DB                        test rbx, rbx
006FE294  74 04                           je 0x1406fe29a
006FE296  C6 43 0A 01                     mov byte ptr [rbx + 0xa], 1
006FE29A  48 83 C4 20                     add rsp, 0x20
006FE29E  5B                              pop rbx
006FE29F  C3                              ret
006FE2A0  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpLockGlobalKeyLockTrackerShared(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_rip + 8353294, a2, a3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = v_rip + 8353248;
        a3 = 0;
        a2 = 0;
        a1 = v_rip + 8353236;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
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
int64_t CmpLockGlobalKeyLockTrackerShared(int64_t Arg1, int32_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(v_rip + 8353294, Arg2, Arg3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = v_rip + 8353248;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = v_rip + 8353236;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, a4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x006FE23C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006FE23C[BB_006FE23C]
  bb_006FE279[BB_006FE279]
  bb_006FE291[BB_006FE291]
  bb_006FE296[BB_006FE296]
  bb_006FE29A[BB_006FE29A]
  bb_006FE2A0[BB_006FE2A0]
  bb_006FE23C -->|branch| bb_006FE291
  bb_006FE23C -->|fallthrough| bb_006FE279
  bb_006FE279 -->|flow| bb_006FE291
  bb_006FE291 -->|branch| bb_006FE29A
  bb_006FE291 -->|fallthrough| bb_006FE296
  bb_006FE296 -->|flow| bb_006FE29A
```

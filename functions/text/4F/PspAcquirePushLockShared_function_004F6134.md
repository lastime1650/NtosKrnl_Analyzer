# PspAcquirePushLockShared

- RVA: `0x004F6134`–`0x004F6199` (길이 `101` bytes)
- VA: `0x00000001404F6134`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `26`개 명령, `101/101` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x004F6157` → [KeAbPreAcquire](../21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x004F6184` → [ExfAcquirePushLockSharedEx](../21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)

### Direct callers
- [PspCompleteServerSiloShutdownDeferred](../../page/77/PspCompleteServerSiloShutdownDeferred_function_0077F860.md) at `0x0077F8CE`
- [PspNotifyServerSiloCreation](../../page/78/PspNotifyServerSiloCreation_function_00786C58.md) at `0x00786C80`
- [PspBeginServerSiloShutdown](../../page/AD/PspBeginServerSiloShutdown_function_00AD2B7C.md) at `0x00AD2BA5`

### Static image references
- `0x004F6143` → RVA `0x00FD9B60` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004F6134  40 53                           push rbx
004F6136  48 83 EC 20                     sub rsp, 0x20
004F613A  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
004F6143  48 8D 0D 16 3A AE 00            lea rcx, [rip + 0xae3a16]
004F614A  45 33 C0                        xor r8d, r8d
004F614D  33 D2                           xor edx, edx
004F614F  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
004F6156  90                              nop
004F6157  E8 D4 A0 D1 FF                  call 0x140210230
004F615C  48 8B D8                        mov rbx, rax
004F615F  BA 11 00 00 00                  mov edx, 0x11
004F6164  33 C0                           xor eax, eax
004F6166  F0 48 0F B1 15 F1 39 AE 00      lock cmpxchg qword ptr [rip + 0xae39f1], rdx
004F616F  74 18                           je 0x1404f6189
004F6171  4C 8D 0D E8 39 AE 00            lea r9, [rip + 0xae39e8]
004F6178  4C 8B C3                        mov r8, rbx
004F617B  33 D2                           xor edx, edx
004F617D  48 8D 0D DC 39 AE 00            lea rcx, [rip + 0xae39dc]
004F6184  E8 C3 A2 D1 FF                  call 0x14021044c
004F6189  48 85 DB                        test rbx, rbx
004F618C  74 04                           je 0x1404f6192
004F618E  C6 43 0A 01                     mov byte ptr [rbx + 0xa], 1
004F6192  48 83 C4 20                     add rsp, 0x20
004F6196  5B                              pop rbx
004F6197  C3                              ret
004F6198  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PspAcquirePushLockShared(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_rip + 11418134, a2, a3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = v_rip + 11418088;
        a3 = 0;
        a2 = 0;
        a1 = v_rip + 11418076;
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
int64_t PspAcquirePushLockShared(int64_t Arg1, int32_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(v_rip + 11418134, Arg2, Arg3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = v_rip + 11418088;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = v_rip + 11418076;
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

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004F6134&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004F6134[BB_004F6134]
  bb_004F6171[BB_004F6171]
  bb_004F6189[BB_004F6189]
  bb_004F618E[BB_004F618E]
  bb_004F6192[BB_004F6192]
  bb_004F6198[BB_004F6198]
  bb_004F6134 -->|branch| bb_004F6189
  bb_004F6134 -->|fallthrough| bb_004F6171
  bb_004F6171 -->|flow| bb_004F6189
  bb_004F6189 -->|branch| bb_004F6192
  bb_004F6189 -->|fallthrough| bb_004F618E
  bb_004F618E -->|flow| bb_004F6192
```

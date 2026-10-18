# ObpLockDirectoryShared

- RVA: `0x0099EF20`–`0x0099EF8C` (길이 `108` bytes)
- VA: `0x000000014099EF20`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00068D5C`
- 디코드: `31`개 명령, `108/108` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0099EF51` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0099EF72` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)

### Direct callers
- [ObpCreateSymbolicLinkName](../74/ObpCreateSymbolicLinkName_function_0074EB80.md) at `0x0074ECAE`
- [NtQueryDirectoryObject](NtQueryDirectoryObject_function_0099EA20.md) at `0x0099EB78`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x0099EF51` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0099EF72` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0099EF20  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
0099EF25  57                              push rdi
0099EF26  48 83 EC 20                     sub rsp, 0x20
0099EF2A  48 89 11                        mov qword ptr [rcx], rdx
0099EF2D  48 8D BA 28 01 00 00            lea rdi, [rdx + 0x128]
0099EF34  C6 41 15 00                     mov byte ptr [rcx + 0x15], 0
0099EF38  45 33 C0                        xor r8d, r8d
0099EF3B  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0099EF44  33 D2                           xor edx, edx
0099EF46  48 8B CF                        mov rcx, rdi
0099EF49  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
0099EF50  90                              nop
0099EF51  E8 DA 12 87 FF                  call 0x140210230
0099EF56  48 8B D8                        mov rbx, rax
0099EF59  B9 11 00 00 00                  mov ecx, 0x11
0099EF5E  33 C0                           xor eax, eax
0099EF60  F0 48 0F B1 0F                  lock cmpxchg qword ptr [rdi], rcx
0099EF65  74 10                           je 0x14099ef77
0099EF67  4C 8B CF                        mov r9, rdi
0099EF6A  4C 8B C3                        mov r8, rbx
0099EF6D  33 D2                           xor edx, edx
0099EF6F  48 8B CF                        mov rcx, rdi
0099EF72  E8 D5 14 87 FF                  call 0x14021044c
0099EF77  48 85 DB                        test rbx, rbx
0099EF7A  74 04                           je 0x14099ef80
0099EF7C  C6 43 0A 01                     mov byte ptr [rbx + 0xa], 1
0099EF80  48 8B 5C 24 38                  mov rbx, qword ptr [rsp + 0x38]
0099EF85  48 83 C4 20                     add rsp, 0x20
0099EF89  5F                              pop rdi
0099EF8A  C3                              ret
0099EF8B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ObpLockDirectoryShared(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;

    v_stack_p10 = v_rbx;
    v_rsp = (v_rsp) - (32);
    *(unsigned __int64 *)(a1) = a2;
    *(unsigned __int8 *)(a1 + 21) = 0;
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(a2 + 296, a2, a3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = a2 + 296;
        a3 = 0;
        a2 = 0;
        a1 = a2 + 296;
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
int64_t ObpLockDirectoryShared(void *Arg1, void *Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;

    v_stack_p10 = local_rbx;
    local_rsp = (local_rsp) - (32);
    *(void **)(arg1) = Arg2;
    *(uint8_t *)(arg1 + 0x15) = 0;
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(Arg2 + 296, Arg2, Arg3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = Arg2 + 296;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = Arg2 + 296;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, a4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `W` |
| `Arg1` | `+ 0x15` | `8` | `W` |
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x128` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0099EF20&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0099EF20[BB_0099EF20]
  bb_0099EF67[BB_0099EF67]
  bb_0099EF77[BB_0099EF77]
  bb_0099EF7C[BB_0099EF7C]
  bb_0099EF80[BB_0099EF80]
  bb_0099EF8B[BB_0099EF8B]
  bb_0099EF20 -->|branch| bb_0099EF77
  bb_0099EF20 -->|fallthrough| bb_0099EF67
  bb_0099EF67 -->|flow| bb_0099EF77
  bb_0099EF77 -->|branch| bb_0099EF80
  bb_0099EF77 -->|fallthrough| bb_0099EF7C
  bb_0099EF7C -->|flow| bb_0099EF80
```

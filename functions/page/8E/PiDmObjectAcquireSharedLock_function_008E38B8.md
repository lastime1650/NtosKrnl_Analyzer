# PiDmObjectAcquireSharedLock

- RVA: `0x008E38B8`–`0x008E3916` (길이 `94` bytes)
- VA: `0x00000001408E38B8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00068D5C`
- 디코드: `28`개 명령, `94/94` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **10**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x008E38DB` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x008E38FC` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)

### Direct callers
- [PiDmListRemoveObject](../70/PiDmListRemoveObject_function_007045E8.md) at `0x00704622`
- [PiDmListRemoveList](../73/PiDmListRemoveList_function_00730474.md) at `0x007304B1`
- [PiDmListRemoveList](../73/PiDmListRemoveList_function_00730474.md) at `0x007304BD`
- [PiDmListRemoveList](../73/PiDmListRemoveList_function_00730474.md) at `0x007304D6`
- [sub_008E2AB2](Unknown_function_008E2AB2.md) at `0x008E2CC3`
- [PiDmEnumObjectsWithCallback](PiDmEnumObjectsWithCallback_function_008E3920.md) at `0x008E3A1C`
- [PiDmListEnumObjectsWithCallback](PiDmListEnumObjectsWithCallback_function_008E3B60.md) at `0x008E3BB4`
- [PiDmObjectIsEnumerable](PiDmObjectIsEnumerable_function_008E6458.md) at `0x008E6465`
- [PiDmObjectGetCachedObjectReference](../8F/PiDmObjectGetCachedObjectReference_function_008F7FB0.md) at `0x008F800F`
- [PiDmListAddList](../94/PiDmListAddList_function_0094F4F8.md) at `0x0094F52F`
- [PiDmListAddList](../94/PiDmListAddList_function_0094F4F8.md) at `0x0094F57E`
- [PiDmListAddList](../94/PiDmListAddList_function_0094F4F8.md) at `0x0094F58C`
- [PiDmListAddObject](../95/PiDmListAddObject_function_00950128.md) at `0x00950162`
- [IopRegisterDeviceInterface](../95/IopRegisterDeviceInterface_function_009501B0.md) at `0x009505D4`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x008E38DB` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x008E38FC` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008E38B8  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
008E38BD  57                              push rdi
008E38BE  48 83 EC 20                     sub rsp, 0x20
008E38C2  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008E38CB  45 33 C0                        xor r8d, r8d
008E38CE  33 D2                           xor edx, edx
008E38D0  48 8B F9                        mov rdi, rcx
008E38D3  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
008E38DA  90                              nop
008E38DB  E8 50 C9 92 FF                  call 0x140210230
008E38E0  48 8B D8                        mov rbx, rax
008E38E3  B9 11 00 00 00                  mov ecx, 0x11
008E38E8  33 C0                           xor eax, eax
008E38EA  F0 48 0F B1 0F                  lock cmpxchg qword ptr [rdi], rcx
008E38EF  74 10                           je 0x1408e3901
008E38F1  4C 8B CF                        mov r9, rdi
008E38F4  4C 8B C3                        mov r8, rbx
008E38F7  33 D2                           xor edx, edx
008E38F9  48 8B CF                        mov rcx, rdi
008E38FC  E8 4B CB 92 FF                  call 0x14021044c
008E3901  48 85 DB                        test rbx, rbx
008E3904  74 04                           je 0x1408e390a
008E3906  C6 43 0A 01                     mov byte ptr [rbx + 0xa], 1
008E390A  48 8B 5C 24 38                  mov rbx, qword ptr [rsp + 0x38]
008E390F  48 83 C4 20                     add rsp, 0x20
008E3913  5F                              pop rdi
008E3914  C3                              ret
008E3915  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiDmObjectAcquireSharedLock(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;

    v_stack_p10 = v_rbx;
    v_rsp = (v_rsp) - (32);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(a1, a2, a3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = a1;
        a3 = 0;
        a2 = 0;
        a1 = a1;
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
int64_t PiDmObjectAcquireSharedLock(void *Arg1, int32_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;

    v_stack_p10 = local_rbx;
    local_rsp = (local_rsp) - (32);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(Arg1, Arg2, Arg3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = Arg1;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = Arg1;
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
| `Arg1` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008E38B8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_008E38B8[BB_008E38B8]
  bb_008E38F1[BB_008E38F1]
  bb_008E3901[BB_008E3901]
  bb_008E3906[BB_008E3906]
  bb_008E390A[BB_008E390A]
  bb_008E3915[BB_008E3915]
  bb_008E38B8 -->|branch| bb_008E3901
  bb_008E38B8 -->|fallthrough| bb_008E38F1
  bb_008E38F1 -->|flow| bb_008E3901
  bb_008E3901 -->|branch| bb_008E390A
  bb_008E3901 -->|fallthrough| bb_008E3906
  bb_008E3906 -->|flow| bb_008E390A
```

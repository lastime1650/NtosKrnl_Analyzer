# RtlpAcquirePropStoreLockShared

- RVA: `0x005E850C`–`0x005E854C` (길이 `64` bytes)
- VA: `0x00000001405E850C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `19`개 명령, `64/64` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x005E8531` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x005E8539` → [ExAcquireSpinLockSharedAtDpcLevel](../24/ExAcquireSpinLockSharedAtDpcLevel_function_00248E30.md) (function, `0x00248E30`)

### Direct callers
- [RtlQueryPointerMapping](RtlQueryPointerMapping_function_005E81A0.md) at `0x005E81BC`
- [RtlQueryPropertyStore](RtlQueryPropertyStore_function_005E8260.md) at `0x005E8281`

### Static image references
- `0x005E8526` → RVA `0x00FC6D20` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005E850C  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
005E8511  57                              push rdi
005E8512  48 83 EC 20                     sub rsp, 0x20
005E8516  48 8B F9                        mov rdi, rcx
005E8519  44 0F 20 C3                     mov rbx, cr8
005E851D  BA 0F 00 00 00                  mov edx, 0xf
005E8522  44 0F 22 C2                     mov cr8, rdx
005E8526  83 3D F3 E7 9D 00 00            cmp dword ptr [rip + 0x9de7f3], 0
005E852D  74 07                           je 0x1405e8536
005E852F  8A CB                           mov cl, bl
005E8531  E8 C6 D1 F0 FF                  call 0x1404f56fc
005E8536  48 8B CF                        mov rcx, rdi
005E8539  E8 F2 08 C6 FF                  call 0x140248e30
005E853E  8A C3                           mov al, bl
005E8540  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
005E8545  48 83 C4 20                     add rsp, 0x20
005E8549  5F                              pop rdi
005E854A  C3                              ret
005E854B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlpAcquirePropStoreLockShared(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    if ((*(unsigned int *)(v_rip + 10348531)) != 0) {
        a1 = (unsigned __int8)(v_cr8);
        result = KiRaiseIrqlProcessIrqlFlags(a1, 15, a3, a4);
    }
    result = ExAcquireSpinLockSharedAtDpcLevel(a1, 15, a3, a4);
    v_rsp = (v_rsp) + (32);
    return (unsigned __int8)(v_cr8);
}
```

## 5. (Beta) C Style

```c
int64_t RtlpAcquirePropStoreLockShared(int64_t Arg1)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    if ((*(uint32_t *)(v_rip + 0x9DE7F3)) != 0) {
        Arg1 = (uint8_t)(v_cr8);
        result = KiRaiseIrqlProcessIrqlFlags(Arg1, 15, a3, a4);
    }
    result = ExAcquireSpinLockSharedAtDpcLevel(Arg1, 15, a3, a4);
    local_rsp = (local_rsp) + (32);
    return (uint8_t)(v_cr8);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005E850C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005E850C[BB_005E850C]
  bb_005E852F[BB_005E852F]
  bb_005E8536[BB_005E8536]
  bb_005E854B[BB_005E854B]
  bb_005E850C -->|branch| bb_005E8536
  bb_005E850C -->|fallthrough| bb_005E852F
  bb_005E852F -->|flow| bb_005E8536
```

# RtlpAcquirePropStoreLockExclusive

- RVA: `0x005E84C4`–`0x005E8504` (길이 `64` bytes)
- VA: `0x00000001405E84C4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `19`개 명령, `64/64` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x005E84E9` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x005E84F1` → [ExAcquireSpinLockExclusiveAtDpcLevel](../24/ExAcquireSpinLockExclusiveAtDpcLevel_function_00248E80.md) (function, `0x00248E80`)

### Direct callers
- [RtlCompareExchangePointerMapping](RtlCompareExchangePointerMapping_function_005E7E20.md) at `0x005E7E6D`
- [RtlCompareExchangePropertyStore](RtlCompareExchangePropertyStore_function_005E7F70.md) at `0x005E7FA4`
- [RtlCompareExchangePropertyStore](RtlCompareExchangePropertyStore_function_005E7F70.md) at `0x005E8062`
- [RtlRemovePointerMapping](RtlRemovePointerMapping_function_005E8300.md) at `0x005E8321`
- [RtlRemovePropertyStore](RtlRemovePropertyStore_function_005E83E0.md) at `0x005E8402`

### Static image references
- `0x005E84DE` → RVA `0x00FC6D20` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005E84C4  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
005E84C9  57                              push rdi
005E84CA  48 83 EC 20                     sub rsp, 0x20
005E84CE  48 8B F9                        mov rdi, rcx
005E84D1  44 0F 20 C3                     mov rbx, cr8
005E84D5  BA 0F 00 00 00                  mov edx, 0xf
005E84DA  44 0F 22 C2                     mov cr8, rdx
005E84DE  83 3D 3B E8 9D 00 00            cmp dword ptr [rip + 0x9de83b], 0
005E84E5  74 07                           je 0x1405e84ee
005E84E7  8A CB                           mov cl, bl
005E84E9  E8 0E D2 F0 FF                  call 0x1404f56fc
005E84EE  48 8B CF                        mov rcx, rdi
005E84F1  E8 8A 09 C6 FF                  call 0x140248e80
005E84F6  8A C3                           mov al, bl
005E84F8  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
005E84FD  48 83 C4 20                     add rsp, 0x20
005E8501  5F                              pop rdi
005E8502  C3                              ret
005E8503  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlpAcquirePropStoreLockExclusive(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    if ((*(unsigned int *)(v_rip + 10348603)) != 0) {
        a1 = (unsigned __int8)(v_cr8);
        result = KiRaiseIrqlProcessIrqlFlags(a1, 15, a3, a4);
    }
    result = ExAcquireSpinLockExclusiveAtDpcLevel(a1, 15, a3, a4);
    v_rsp = (v_rsp) + (32);
    return (unsigned __int8)(v_cr8);
}
```

## 5. (Beta) C Style

```c
int64_t RtlpAcquirePropStoreLockExclusive(int64_t Arg1)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    if ((*(uint32_t *)(v_rip + 0x9DE83B)) != 0) {
        Arg1 = (uint8_t)(v_cr8);
        result = KiRaiseIrqlProcessIrqlFlags(Arg1, 15, a3, a4);
    }
    result = ExAcquireSpinLockExclusiveAtDpcLevel(Arg1, 15, a3, a4);
    local_rsp = (local_rsp) + (32);
    return (uint8_t)(v_cr8);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005E84C4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005E84C4[BB_005E84C4]
  bb_005E84E7[BB_005E84E7]
  bb_005E84EE[BB_005E84EE]
  bb_005E8503[BB_005E8503]
  bb_005E84C4 -->|branch| bb_005E84EE
  bb_005E84C4 -->|fallthrough| bb_005E84E7
  bb_005E84E7 -->|flow| bb_005E84EE
```

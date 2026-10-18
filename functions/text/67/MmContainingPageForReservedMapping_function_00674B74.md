# MmContainingPageForReservedMapping

- RVA: `0x00674B74`–`0x00674BA1` (길이 `45` bytes)
- VA: `0x0000000140674B74`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `10`개 명령, `45/45` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00674B96` → [MiGetContainingPageTable](../34/MiGetContainingPageTable_function_003467F0.md) (function, `0x003467F0`)

### Direct callers
- [PnprCopyReservedMapping](../5A/PnprCopyReservedMapping_function_005A8864.md) at `0x005A8958`
- [PnprCopyReservedMapping](../5A/PnprCopyReservedMapping_function_005A8864.md) at `0x005A8A42`
- [PnprRecopyMappingReserve](../5A/PnprRecopyMappingReserve_function_005A8EE8.md) at `0x005A8F0F`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00674B74  48 83 EC 28                     sub rsp, 0x28
00674B78  48 C1 E9 09                     shr rcx, 9
00674B7C  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
00674B86  48 23 C8                        and rcx, rax
00674B89  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
00674B93  48 03 C8                        add rcx, rax
00674B96  E8 55 1C CD FF                  call 0x1403467f0
00674B9B  48 83 C4 28                     add rsp, 0x28
00674B9F  C3                              ret
00674BA0  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MmContainingPageForReservedMapping(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a1 = (a1) >> (9);
    a1 = (a1) & (result);
    a1 = (a1) + (result);
    result = MiGetContainingPageTable(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MmContainingPageForReservedMapping(int64_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg1 = (Arg1) >> (9);
    Arg1 = (Arg1) & (result);
    Arg1 = (Arg1) + (result);
    result = MiGetContainingPageTable(Arg1, a2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00674B74&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00674B74[BB_00674B74]
  bb_00674BA0[BB_00674BA0]
```

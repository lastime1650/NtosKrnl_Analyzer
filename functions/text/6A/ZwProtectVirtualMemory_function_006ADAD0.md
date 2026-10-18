# ZwProtectVirtualMemory

- RVA: `0x006ADAD0`–`0x006ADAEF` (길이 `31` bytes)
- VA: `0x00000001406ADAD0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C0250`
- 디코드: `11`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [CmSiProtectViewOfSection](../47/CmSiProtectViewOfSection_function_004746B8.md) at `0x004746E4`
- [KiOpPatchCode](../5C/KiOpPatchCode_function_005C6900.md) at `0x005C6979`
- [KiOpPatchCode](../5C/KiOpPatchCode_function_005C6900.md) at `0x005C6A6D`
- [DifZwProtectVirtualMemoryWrapper](../64/DifZwProtectVirtualMemoryWrapper_function_00645AE0.md) at `0x00645BEA`
- [WbMakeUserDataPagesKernelWritable](../../page/9A/WbMakeUserDataPagesKernelWritable_function_009A15FC.md) at `0x009A1650`
- [MiCheckForUserStackOverflow](../../page/A3/MiCheckForUserStackOverflow_function_00A30854.md) at `0x00A30AC4`

### Static image references
- `0x006ADADC` → RVA `0x006B3460` (`KiServiceLinkage`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006ADAE9` → [KiServiceInternal](../6C/KiServiceInternal_function_006C49C0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006ADAD0  48 8B C4                        mov rax, rsp
006ADAD3  FA                              cli
006ADAD4  48 83 EC 10                     sub rsp, 0x10
006ADAD8  50                              push rax
006ADAD9  9C                              pushfq
006ADADA  6A 10                           push 0x10
006ADADC  48 8D 05 7D 59 00 00            lea rax, [rip + 0x597d]
006ADAE3  50                              push rax
006ADAE4  B8 50 00 00 00                  mov eax, 0x50
006ADAE9  E9 D2 6E 01 00                  jmp 0x1406c49c0
006ADAEE  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ZwProtectVirtualMemory(void)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) - (16);
}
```

## 5. (Beta) C Style

```c
void ZwProtectVirtualMemory(void)
{
    int64_t local_rsp;

    local_rsp = (local_rsp) - (16);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006ADAD0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006ADAD0[BB_006ADAD0]
  bb_006ADAEE[BB_006ADAEE]
```

# ZwAdjustPrivilegesToken

- RVA: `0x006AD8F0`–`0x006AD90F` (길이 `31` bytes)
- VA: `0x00000001406AD8F0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C019C`
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
- [DifZwAdjustPrivilegesTokenWrapper](../63/DifZwAdjustPrivilegesTokenWrapper_function_0063D6F0.md) at `0x0063D807`
- [RtlAcquirePrivilege](../../page/87/RtlAcquirePrivilege_function_00879120.md) at `0x0087929F`
- [BiAdjustPrivilege](../../page/A3/BiAdjustPrivilege_function_00A3D708.md) at `0x00A3D7A0`
- [RtlReleasePrivilege](../../page/A6/RtlReleasePrivilege_function_00A685A0.md) at `0x00A685D2`
- [sub_00B17FC0](../../page/B1/Unknown_function_00B17FC0.md) at `0x00B18003`

### Static image references
- `0x006AD8FC` → RVA `0x006B3460` (`KiServiceLinkage`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006AD909` → [KiServiceInternal](../6C/KiServiceInternal_function_006C49C0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006AD8F0  48 8B C4                        mov rax, rsp
006AD8F3  FA                              cli
006AD8F4  48 83 EC 10                     sub rsp, 0x10
006AD8F8  50                              push rax
006AD8F9  9C                              pushfq
006AD8FA  6A 10                           push 0x10
006AD8FC  48 8D 05 5D 5B 00 00            lea rax, [rip + 0x5b5d]
006AD903  50                              push rax
006AD904  B8 41 00 00 00                  mov eax, 0x41
006AD909  E9 B2 70 01 00                  jmp 0x1406c49c0
006AD90E  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ZwAdjustPrivilegesToken(void)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) - (16);
}
```

## 5. (Beta) C Style

```c
void ZwAdjustPrivilegesToken(void)
{
    int64_t local_rsp;

    local_rsp = (local_rsp) - (16);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006AD8F0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006AD8F0[BB_006AD8F0]
  bb_006AD90E[BB_006AD90E]
```

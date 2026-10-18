# ZwCreateThreadEx

- RVA: `0x006AE9F0`–`0x006AEA0F` (길이 `31` bytes)
- VA: `0x00000001406AE9F0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C07FC`
- 디코드: `11`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [DbgkUserReportWorkRoutine](../../page/71/DbgkUserReportWorkRoutine_function_00710D10.md) at `0x00710F33`
- [MiInjectThreadForHotPatch](../../page/80/MiInjectThreadForHotPatch_function_00803FD8.md) at `0x008040B5`
- [RtlpCreateUserThreadEx](../../page/A1/RtlpCreateUserThreadEx_function_00A1E5D4.md) at `0x00A1E720`
- [MiForceCrashForInvalidAccess](../../page/AC/MiForceCrashForInvalidAccess_function_00ACEFA4.md) at `0x00ACF135`

### Static image references
- `0x006AE9FC` → RVA `0x006B3460` (`KiServiceLinkage`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006AEA09` → [KiServiceInternal](../6C/KiServiceInternal_function_006C49C0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006AE9F0  48 8B C4                        mov rax, rsp
006AE9F3  FA                              cli
006AE9F4  48 83 EC 10                     sub rsp, 0x10
006AE9F8  50                              push rax
006AE9F9  9C                              pushfq
006AE9FA  6A 10                           push 0x10
006AE9FC  48 8D 05 5D 4A 00 00            lea rax, [rip + 0x4a5d]
006AEA03  50                              push rax
006AEA04  B8 C9 00 00 00                  mov eax, 0xc9
006AEA09  E9 B2 5F 01 00                  jmp 0x1406c49c0
006AEA0E  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ZwCreateThreadEx(void)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) - (16);
}
```

## 5. (Beta) C Style

```c
void ZwCreateThreadEx(void)
{
    int64_t local_rsp;

    local_rsp = (local_rsp) - (16);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006AE9F0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006AE9F0[BB_006AE9F0]
  bb_006AEA0E[BB_006AEA0E]
```

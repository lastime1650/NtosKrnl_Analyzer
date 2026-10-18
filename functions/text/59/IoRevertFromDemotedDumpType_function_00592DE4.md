# IoRevertFromDemotedDumpType

- RVA: `0x00592DE4`–`0x00592E07` (길이 `35` bytes)
- VA: `0x0000000140592DE4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `11`개 명령, `35/35` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00592DFC` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [KiAttemptBugcheckRecovery](../5C/KiAttemptBugcheckRecovery_function_005C6D24.md) at `0x005C6FC4`
- [KiBugCheckRecoveryPrepareForCrashDump](../5C/KiBugCheckRecoveryPrepareForCrashDump_function_005C7410.md) at `0x005C744D`

### Static image references
- `0x00592DE8` → RVA `0x00E66000` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00592DE4  48 83 EC 28                     sub rsp, 0x28
00592DE8  48 8B 05 11 32 8D 00            mov rax, qword ptr [rip + 0x8d3211]
00592DEF  48 85 C0                        test rax, rax
00592DF2  74 0D                           je 0x140592e01
00592DF4  33 D2                           xor edx, edx
00592DF6  45 33 C0                        xor r8d, r8d
00592DF9  8D 4A 08                        lea ecx, [rdx + 8]
00592DFC  E8 CF 7C 12 00                  call 0x1406baad0
00592E01  48 83 C4 28                     add rsp, 0x28
00592E05  C3                              ret
00592E06  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IoRevertFromDemotedDumpType(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = *(unsigned __int64 *)(v_rip + 9253393);
    if (*(unsigned __int64 *)(v_rip + 9253393) != 0) {
        a2 = 0;
        a3 = 0;
        a1 = a2 + 8;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t IoRevertFromDemotedDumpType(int64_t Arg1, int32_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = *(uint64_t *)(v_rip + 0x8D3211);
    if (*(uint64_t *)(v_rip + 0x8D3211) != 0) {
        Arg2 = 0;
        Arg3 = 0;
        Arg1 = Arg2 + 8;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00592DE4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00592DE4[BB_00592DE4]
  bb_00592DF4[BB_00592DF4]
  bb_00592E01[BB_00592E01]
  bb_00592E06[BB_00592E06]
  bb_00592DE4 -->|branch| bb_00592E01
  bb_00592DE4 -->|fallthrough| bb_00592DF4
  bb_00592DF4 -->|flow| bb_00592E01
```

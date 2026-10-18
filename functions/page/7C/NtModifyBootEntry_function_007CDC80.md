# NtModifyBootEntry

- RVA: `0x007CDC80`–`0x007CDCA7` (길이 `39` bytes)
- VA: `0x00000001407CDC80`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `12`개 명령, `39/39` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x007CDC9C` → [ExpSetBootEntry](ExpSetBootEntry_function_007CBD2C.md) (function, `0x007CBD2C`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x007CDC84` → RVA `0x00EFF050` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007CDC80  48 83 EC 28                     sub rsp, 0x28
007CDC84  83 3D C5 13 73 00 02            cmp dword ptr [rip + 0x7313c5], 2
007CDC8B  74 07                           je 0x1407cdc94
007CDC8D  B8 02 00 00 C0                  mov eax, 0xc0000002
007CDC92  EB 0D                           jmp 0x1407cdca1
007CDC94  48 8B D1                        mov rdx, rcx
007CDC97  45 33 C0                        xor r8d, r8d
007CDC9A  33 C9                           xor ecx, ecx
007CDC9C  E8 8B E0 FF FF                  call 0x1407cbd2c
007CDCA1  48 83 C4 28                     add rsp, 0x28
007CDCA5  C3                              ret
007CDCA6  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtModifyBootEntry(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if ((*(unsigned int *)(v_rip + 7541701)) == 2) goto loc_007CDC94;
    goto loc_007CDCA1;
loc_007CDC94:
    a3 = 0;
    a1 = 0;
    result = ExpSetBootEntry(a1, a1, a3, a4);
loc_007CDCA1:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t NtModifyBootEntry(int64_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if ((*(uint32_t *)(v_rip + 0x7313C5)) == 2) goto loc_007CDC94;
    goto loc_007CDCA1;
loc_007CDC94:
    Arg3 = 0;
    Arg1 = 0;
    result = ExpSetBootEntry(Arg1, Arg1, Arg3, a4);
loc_007CDCA1:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007CDC80&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007CDC80[BB_007CDC80]
  bb_007CDC8D[BB_007CDC8D]
  bb_007CDC94[BB_007CDC94]
  bb_007CDCA1[BB_007CDCA1]
  bb_007CDCA6[BB_007CDCA6]
  bb_007CDC80 -->|branch| bb_007CDC94
  bb_007CDC80 -->|fallthrough| bb_007CDC8D
  bb_007CDC8D -->|branch| bb_007CDCA1
  bb_007CDC94 -->|flow| bb_007CDCA1
```

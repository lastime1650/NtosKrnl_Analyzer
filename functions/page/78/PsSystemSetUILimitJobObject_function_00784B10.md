# PsSystemSetUILimitJobObject

- RVA: `0x00784B10`–`0x00784B31` (길이 `33` bytes)
- VA: `0x0000000140784B10`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `8`개 명령, `33/33` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00784B26` → [PspSetUILimitJobObject](../6F/PspSetUILimitJobObject_function_006FD218.md) (function, `0x006FD218`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00784B10  48 83 EC 28                     sub rsp, 0x28
00784B14  44 8B C2                        mov r8d, edx
00784B17  41 B9 01 00 00 00               mov r9d, 1
00784B1D  65 48 8B 14 25 88 01 00 00      mov rdx, qword ptr gs:[0x188]
00784B26  E8 ED 86 F7 FF                  call 0x1406fd218
00784B2B  48 83 C4 28                     add rsp, 0x28
00784B2F  C3                              ret
00784B30  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PsSystemSetUILimitJobObject(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = PspSetUILimitJobObject(a1, *(unsigned __int64 *)(gs_base + (0 + 392)), (unsigned int)(a2), 1);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PsSystemSetUILimitJobObject(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = PspSetUILimitJobObject(Arg1, *(uint64_t *)(gs_base + (0 + 0x188)), (uint32_t)(Arg2), 1);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00784B10&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00784B10[BB_00784B10]
  bb_00784B30[BB_00784B30]
```

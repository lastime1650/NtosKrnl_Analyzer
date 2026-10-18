# BgpDisplayCharacterDestroyContext

- RVA: `0x00BC0834`–`0x00BC0859` (길이 `37` bytes)
- VA: `0x0000000140BC0834`
- 실행 섹션: `PAGEBGFX`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000805BC`
- 디코드: `13`개 명령, `37/37` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00BC0845` → [BgpTxtDestroyRegion](BgpTxtDestroyRegion_function_00BC2B5C.md) (function, `0x00BC2B5C`)
- `0x00BC084D` → [BgpFwFreeMemory](../../text/3E/BgpFwFreeMemory_function_003E25E0.md) (function, `0x003E25E0`)

### Direct callers
- [BgConsoleDestroyInterface](BgConsoleDestroyInterface_function_00BC0940.md) at `0x00BC0972`
- [BgpBcInitializeCriticalMode](../../init/C8/BgpBcInitializeCriticalMode_function_00C81454.md) at `0x00C81A10`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00BC084D` → [BgpFwFreeMemory](../../text/3E/BgpFwFreeMemory_function_003E25E0.md) (`PAGEBGFX` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BC0834  48 85 C9                        test rcx, rcx
00BC0837  74 1E                           je 0x140bc0857
00BC0839  53                              push rbx
00BC083A  48 83 EC 20                     sub rsp, 0x20
00BC083E  48 8B D9                        mov rbx, rcx
00BC0841  48 8B 49 18                     mov rcx, qword ptr [rcx + 0x18]
00BC0845  E8 12 23 00 00                  call 0x140bc2b5c
00BC084A  48 8B CB                        mov rcx, rbx
00BC084D  E8 8E 1D 82 FF                  call 0x1403e25e0
00BC0852  48 83 C4 20                     add rsp, 0x20
00BC0856  5B                              pop rbx
00BC0857  C3                              ret
00BC0858  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall BgpDisplayCharacterDestroyContext(__int64 a1)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;

    if (a1 != 0) {
        v_rsp = (v_rsp) - (32);
        v_rbx = a1;
        a1 = *(unsigned __int64 *)(a1 + 24);
        result = BgpTxtDestroyRegion(a1, a2, a3, a4);
        a1 = v_rbx;
        result = BgpFwFreeMemory(a1, a2, a3, a4);
        v_rsp = (v_rsp) + (32);
    }
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t BgpDisplayCharacterDestroyContext(int64_t Arg1)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;

    if (Arg1 != 0) {
        local_rsp = (local_rsp) - (32);
        local_rbx = Arg1;
        Arg1 = *(uint64_t *)(Arg1 + 0x18);
        result = BgpTxtDestroyRegion(Arg1, a2, a3, a4);
        Arg1 = local_rbx;
        result = BgpFwFreeMemory(Arg1, a2, a3, a4);
        local_rsp = (local_rsp) + (32);
    }
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagebgfx&rva=0x00BC0834&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BC0834[BB_00BC0834]
  bb_00BC0839[BB_00BC0839]
  bb_00BC0857[BB_00BC0857]
  bb_00BC0858[BB_00BC0858]
  bb_00BC0834 -->|branch| bb_00BC0857
  bb_00BC0834 -->|fallthrough| bb_00BC0839
  bb_00BC0839 -->|flow| bb_00BC0857
```

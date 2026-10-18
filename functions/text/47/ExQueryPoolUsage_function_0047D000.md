# ExQueryPoolUsage

- RVA: `0x0047D000`–`0x0047D03C` (길이 `60` bytes)
- VA: `0x000000014047D000`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00082420`
- 디코드: `14`개 명령, `60/60` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0047D031` → [ExHeapQueryPoolUsage](ExHeapQueryPoolUsage_function_0047D044.md) (function, `0x0047D044`)

### Direct callers
- [ExpQuerySystemPerformanceInformation](../../page/9D/ExpQuerySystemPerformanceInformation_function_009D648C.md) at `0x009D683E`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0047D000  4C 8B DC                        mov r11, rsp
0047D003  48 83 EC 48                     sub rsp, 0x48
0047D007  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
0047D00F  49 89 43 F0                     mov qword ptr [r11 - 0x10], rax
0047D013  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
0047D01B  49 89 43 E8                     mov qword ptr [r11 - 0x18], rax
0047D01F  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
0047D024  49 89 43 E0                     mov qword ptr [r11 - 0x20], rax
0047D028  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
0047D02D  49 89 43 D8                     mov qword ptr [r11 - 0x28], rax
0047D031  E8 0E 00 00 00                  call 0x14047d044
0047D036  48 83 C4 48                     add rsp, 0x48
0047D03A  C3                              ret
0047D03B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExQueryPoolUsage(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (72);
    *(unsigned __int64 *)(v_rsp - 16) = a8;
    *(unsigned __int64 *)(v_rsp - 24) = a7;
    *(unsigned __int64 *)(v_rsp - 32) = a6;
    *(unsigned __int64 *)(v_rsp - 40) = a5;
    result = ExHeapQueryPoolUsage(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (72);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ExQueryPoolUsage(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, int64_t Arg6, int64_t Arg7, int64_t Arg8)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (72);
    *(uint64_t *)(local_rsp - 0x10) = Arg8;
    *(uint64_t *)(local_rsp - 0x18) = Arg7;
    *(uint64_t *)(local_rsp - 0x20) = Arg6;
    *(uint64_t *)(local_rsp - 0x28) = Arg5;
    result = ExHeapQueryPoolUsage(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (72);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0047D000&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0047D000[BB_0047D000]
  bb_0047D03B[BB_0047D03B]
```

# PspUnlockJobMemoryLimitsExclusive

- RVA: `0x0087D390`–`0x0087D39E` (길이 `14` bytes)
- VA: `0x000000014087D390`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007BEB4`
- 디코드: `5`개 명령, `14/14` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [sub_0087F31F](Unknown_function_0087F31F.md) at `0x0087F3AA`
- [sub_0087F483](Unknown_function_0087F483.md) at `0x0087F549`
- [sub_0087F483](Unknown_function_0087F483.md) at `0x0087F576`
- [NtSetInformationJobObject](../9F/NtSetInformationJobObject_function_009F84C0.md) at `0x009F88BD`
- [NtSetInformationJobObject](../9F/NtSetInformationJobObject_function_009F84C0.md) at `0x009F89DD`
- [NtSetInformationJobObject](../9F/NtSetInformationJobObject_function_009F84C0.md) at `0x009F9D96`
- [NtSetInformationJobObject](../9F/NtSetInformationJobObject_function_009F84C0.md) at `0x009FAA75`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x0087D39C` → [sub_0087D3C9](Unknown_function_0087D3C9.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0087D390  40 53                           push rbx
0087D392  48 83 EC 20                     sub rsp, 0x20
0087D396  49 8B D8                        mov rbx, r8
0087D399  48 3B CA                        cmp rcx, rdx
0087D39C  74 2B                           je 0x14087d3c9
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall PspUnlockJobMemoryLimitsExclusive(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
}
```

## 5. (Beta) C Style

```c
void PspUnlockJobMemoryLimitsExclusive(int64_t Arg1, int64_t Arg2, int64_t Arg3)
{
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0087D390&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0087D390[BB_0087D390]
```

# KeDetachProcess

- RVA: `0x00495420`–`0x0049544A` (길이 `42` bytes)
- VA: `0x0000000140495420`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `10`개 명령, `42/42` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0049543F` → [KiDetachProcess](../21/KiDetachProcess_function_002172A0.md) (function, `0x002172A0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00495420  48 83 EC 28                     sub rsp, 0x28
00495424  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0049542D  80 B9 4A 02 00 00 00            cmp byte ptr [rcx + 0x24a], 0
00495434  74 0E                           je 0x140495444
00495436  48 81 C1 58 02 00 00            add rcx, 0x258
0049543D  33 D2                           xor edx, edx
0049543F  E8 5C 1E D8 FF                  call 0x1402172a0
00495444  48 83 C4 28                     add rsp, 0x28
00495448  C3                              ret
00495449  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KeDetachProcess(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 586)) != 0) {
        a1 = (*(unsigned __int64 *)(gs_base + (0 + 392))) + (600);
        a2 = 0;
        result = KiDetachProcess(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KeDetachProcess(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x24A)) != 0) {
        Arg1 = (*(uint64_t *)(gs_base + (0 + 0x188))) + (600);
        Arg2 = 0;
        result = KiDetachProcess(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00495420&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00495420[BB_00495420]
  bb_00495436[BB_00495436]
  bb_00495444[BB_00495444]
  bb_00495449[BB_00495449]
  bb_00495420 -->|branch| bb_00495444
  bb_00495420 -->|fallthrough| bb_00495436
  bb_00495436 -->|flow| bb_00495444
```

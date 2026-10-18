# KiIntSteerEventTraceControlCallback

- RVA: `0x00747370`–`0x00747389` (길이 `25` bytes)
- VA: `0x0000000140747370`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `8`개 명령, `25/25` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0074737E` → [KiIntSteerLogStatus](../../text/2D/KiIntSteerLogStatus_function_002D6400.md) (function, `0x002D6400`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0074737E` → [KiIntSteerLogStatus](../../text/2D/KiIntSteerLogStatus_function_002D6400.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00747370  48 83 EC 28                     sub rsp, 0x28
00747374  F7 C2 FD FF FF FF               test edx, 0xfffffffd
0074737A  75 07                           jne 0x140747383
0074737C  B1 01                           mov cl, 1
0074737E  E8 7D F0 B8 FF                  call 0x1402d6400
00747383  48 83 C4 28                     add rsp, 0x28
00747387  C3                              ret
00747388  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiIntSteerEventTraceControlCallback(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (((a2) & (0xFFFFFFFDULL)) == 0) {
        a1 = 1;
        result = KiIntSteerLogStatus(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KiIntSteerEventTraceControlCallback(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (((Arg2) & (0xFFFFFFFDULL)) == 0) {
        Arg1 = 1;
        result = KiIntSteerLogStatus(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00747370&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00747370[BB_00747370]
  bb_0074737C[BB_0074737C]
  bb_00747383[BB_00747383]
  bb_00747388[BB_00747388]
  bb_00747370 -->|branch| bb_00747383
  bb_00747370 -->|fallthrough| bb_0074737C
  bb_0074737C -->|flow| bb_00747383
```

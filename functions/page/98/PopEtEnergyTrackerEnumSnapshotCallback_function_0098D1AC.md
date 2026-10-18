# PopEtEnergyTrackerEnumSnapshotCallback

- RVA: `0x0098D1AC`–`0x0098D1CF` (길이 `35` bytes)
- VA: `0x000000014098D1AC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `12`개 명령, `35/35` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0098D1BC` → [PopEtProcessSnapshotUpdate](PopEtProcessSnapshotUpdate_function_0098D430.md) (function, `0x0098D430`)

### Direct callers
- [PopEtEnumEnergyTrackers](PopEtEnumEnergyTrackers_function_0098D150.md) at `0x0098D177`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0098D1AC  40 53                           push rbx
0098D1AE  48 83 EC 20                     sub rsp, 0x20
0098D1B2  48 89 4A 10                     mov qword ptr [rdx + 0x10], rcx
0098D1B6  48 8B DA                        mov rbx, rdx
0098D1B9  48 8B CA                        mov rcx, rdx
0098D1BC  E8 6F 02 00 00                  call 0x14098d430
0098D1C1  48 83 63 10 00                  and qword ptr [rbx + 0x10], 0
0098D1C6  33 C0                           xor eax, eax
0098D1C8  48 83 C4 20                     add rsp, 0x20
0098D1CC  5B                              pop rbx
0098D1CD  C3                              ret
0098D1CE  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopEtEnergyTrackerEnumSnapshotCallback(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    *(unsigned __int64 *)(a2 + 16) = a1;
    result = PopEtProcessSnapshotUpdate(a2, a2, a3, a4);
    result = 0;
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopEtEnergyTrackerEnumSnapshotCallback(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    *(uint64_t *)(arg2 + 0x10) = Arg1;
    result = PopEtProcessSnapshotUpdate(Arg2, Arg2, a3, a4);
    result = 0;
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x10` | `64` | `R/W` |
| `Arg2` | `+ 0x10` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0098D1AC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0098D1AC[BB_0098D1AC]
  bb_0098D1CE[BB_0098D1CE]
```

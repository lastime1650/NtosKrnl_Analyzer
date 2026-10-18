# IopLiveDumpEnterCorralledState

- RVA: `0x0059BA40`–`0x0059BA7A` (길이 `58` bytes)
- VA: `0x000000014059BA40`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `14`개 명령, `58/58` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0059BA60` → [IopLiveDumpCorralProcessors](IopLiveDumpCorralProcessors_function_0059B720.md) (function, `0x0059B720`)
- `0x0059BA67` → [IopLiveDumpGetMillisecondCounter](../3F/IopLiveDumpGetMillisecondCounter_function_003F5964.md) (function, `0x003F5964`)

### Direct callers
- [IopLiveDumpCapture](IopLiveDumpCapture_function_0059AF88.md) at `0x0059AFA1`
- [IopLiveDumpEndMirroringCallback](IopLiveDumpEndMirroringCallback_function_0059B990.md) at `0x0059BA0F`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0059BA40  40 53                           push rbx
0059BA42  48 83 EC 20                     sub rsp, 0x20
0059BA46  48 83 A1 C0 00 00 00 00         and qword ptr [rcx + 0xc0], 0
0059BA4E  48 8B D9                        mov rbx, rcx
0059BA51  48 83 A1 C8 00 00 00 00         and qword ptr [rcx + 0xc8], 0
0059BA59  48 81 C1 38 01 00 00            add rcx, 0x138
0059BA60  E8 BB FC FF FF                  call 0x14059b720
0059BA65  33 C9                           xor ecx, ecx
0059BA67  E8 F8 9E E5 FF                  call 0x1403f5964
0059BA6C  48 89 83 18 02 00 00            mov qword ptr [rbx + 0x218], rax
0059BA73  48 83 C4 20                     add rsp, 0x20
0059BA77  5B                              pop rbx
0059BA78  C3                              ret
0059BA79  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IopLiveDumpEnterCorralledState(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    a1 = (a1) + (312);
    result = IopLiveDumpCorralProcessors(a1, a2, a3, a4);
    a1 = 0;
    result = IopLiveDumpGetMillisecondCounter(a1, a2, a3, a4);
    *(unsigned __int64 *)(a1 + 536) = result;
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t IopLiveDumpEnterCorralledState(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    Arg1 = (Arg1) + (312);
    result = IopLiveDumpCorralProcessors(Arg1, a2, a3, a4);
    Arg1 = 0;
    result = IopLiveDumpGetMillisecondCounter(Arg1, a2, a3, a4);
    *(uint64_t *)(arg1 + 0x218) = result;
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xC0` | `64` | `R/W` |
| `Arg1` | `+ 0xC8` | `64` | `R/W` |
| `Arg1` | `+ 0x218` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0059BA40&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0059BA40[BB_0059BA40]
  bb_0059BA79[BB_0059BA79]
```

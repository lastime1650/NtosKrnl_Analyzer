# ObpDirectoryTeardownCallback

- RVA: `0x0083CEC0`–`0x0083CEF8` (길이 `56` bytes)
- VA: `0x000000014083CEC0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `17`개 명령, `56/56` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0083CECC` → [ObMakeTemporaryObject](../A7/ObMakeTemporaryObject_function_00A7F860.md) (function, `0x00A7F860`)
- `0x0083CED9` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x0083CEEC` → [ObDereferenceDeviceMap](../96/ObDereferenceDeviceMap_function_0096D0E8.md) (function, `0x0096D0E8`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0083CED9` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0083CEC0  40 53                           push rbx
0083CEC2  48 83 EC 20                     sub rsp, 0x20
0083CEC6  48 8B D9                        mov rbx, rcx
0083CEC9  48 8B 09                        mov rcx, qword ptr [rcx]
0083CECC  E8 8F 29 24 00                  call 0x140a7f860
0083CED1  48 8B 0B                        mov rcx, qword ptr [rbx]
0083CED4  BA 4F 62 54 72                  mov edx, 0x7254624f
0083CED9  E8 02 AA AB FF                  call 0x1402f78e0
0083CEDE  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
0083CEE2  48 85 C9                        test rcx, rcx
0083CEE5  74 0A                           je 0x14083cef1
0083CEE7  BA 01 00 00 00                  mov edx, 1
0083CEEC  E8 F7 01 13 00                  call 0x14096d0e8
0083CEF1  48 83 C4 20                     add rsp, 0x20
0083CEF5  5B                              pop rbx
0083CEF6  C3                              ret
0083CEF7  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ObpDirectoryTeardownCallback(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = ObMakeTemporaryObject(*(unsigned __int64 *)(a1), a2, a3, a4);
    result = ObfDereferenceObjectWithTag(*(unsigned __int64 *)(a1), (unsigned int)(0x7254624FULL), a3, a4);
    if (*(unsigned __int64 *)(a1 + 8) != 0) {
        a2 = 1;
        result = ObDereferenceDeviceMap(*(unsigned __int64 *)(a1 + 8), a2, a3, a4);
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ObpDirectoryTeardownCallback(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = ObMakeTemporaryObject(*(uint64_t *)(arg1), a2, a3, a4);
    result = ObfDereferenceObjectWithTag(*(uint64_t *)(arg1), (uint32_t)(0x7254624FULL), a3, a4);
    if (*(uint64_t *)(arg1 + 0x8) != 0) {
        a2 = 1;
        result = ObDereferenceDeviceMap(*(uint64_t *)(arg1 + 0x8), a2, a3, a4);
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0083CEC0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0083CEC0[BB_0083CEC0]
  bb_0083CEE7[BB_0083CEE7]
  bb_0083CEF1[BB_0083CEF1]
  bb_0083CEF7[BB_0083CEF7]
  bb_0083CEC0 -->|branch| bb_0083CEF1
  bb_0083CEC0 -->|fallthrough| bb_0083CEE7
  bb_0083CEE7 -->|flow| bb_0083CEF1
```

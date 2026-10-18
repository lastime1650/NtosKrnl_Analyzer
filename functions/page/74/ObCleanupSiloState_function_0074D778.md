# ObCleanupSiloState

- RVA: `0x0074D778`–`0x0074D79F` (길이 `39` bytes)
- VA: `0x000000014074D778`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `14`개 명령, `39/39` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0074D794` → [ObDereferenceDeviceMap](../96/ObDereferenceDeviceMap_function_0096D0E8.md) (function, `0x0096D0E8`)

### Direct callers
- [ObShutdownSystem](ObShutdownSystem_function_0074DBB0.md) at `0x0074DD1A`
- [PspDeleteExternalServerSiloState](../77/PspDeleteExternalServerSiloState_function_0077FB88.md) at `0x0077FC0D`
- [PspDeleteServerSiloGlobals](../77/PspDeleteServerSiloGlobals_function_0077FC54.md) at `0x0077FC83`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0074D778  48 83 EC 28                     sub rsp, 0x28
0074D77C  48 8B C1                        mov rax, rcx
0074D77F  33 C9                           xor ecx, ecx
0074D781  48 87 08                        xchg qword ptr [rax], rcx
0074D784  48 85 C9                        test rcx, rcx
0074D787  74 10                           je 0x14074d799
0074D789  8B D1                           mov edx, ecx
0074D78B  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
0074D78F  83 E2 0F                        and edx, 0xf
0074D792  FF C2                           inc edx
0074D794  E8 4F F9 21 00                  call 0x14096d0e8
0074D799  48 83 C4 28                     add rsp, 0x28
0074D79D  C3                              ret
0074D79E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ObCleanupSiloState(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a1 = 0;
    result = a1;
    if (0 != 0) {
        a2 = 0;
        a1 = (a1) & (-16);
        a2 = (unsigned int)((a2) & (15));
        a2 = (unsigned int)((a2) + 1);
        result = ObDereferenceDeviceMap(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ObCleanupSiloState(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg1 = 0;
    result = Arg1;
    if (0 != 0) {
        a2 = 0;
        Arg1 = (Arg1) & (-16);
        a2 = (uint32_t)((a2) & (15));
        a2 = (uint32_t)((a2) + 1);
        result = ObDereferenceDeviceMap(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0074D778&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0074D778[BB_0074D778]
  bb_0074D789[BB_0074D789]
  bb_0074D799[BB_0074D799]
  bb_0074D79E[BB_0074D79E]
  bb_0074D778 -->|branch| bb_0074D799
  bb_0074D778 -->|fallthrough| bb_0074D789
  bb_0074D789 -->|flow| bb_0074D799
```

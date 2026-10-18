# VfZwAlpcAcceptConnectPort_Entry

- RVA: `0x00BA3D90`–`0x00BA3DE5` (길이 `85` bytes)
- VA: `0x0000000140BA3D90`
- 실행 섹션: `PAGEVRFY`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `25`개 명령, `85/85` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **6**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00BA3D99` → [ViZwShouldCheck](ViZwShouldCheck_function_00BA4DB4.md) (function, `0x00BA4DB4`)
- `0x00BA3DA9` → [ViZwCheckVirtualAddress](ViZwCheckVirtualAddress_function_00BA4D68.md) (function, `0x00BA4D68`)
- `0x00BA3DB5` → [ViZwCheckVirtualAddress](ViZwCheckVirtualAddress_function_00BA4D68.md) (function, `0x00BA4D68`)
- `0x00BA3DC1` → [ViZwCheckVirtualAddress](ViZwCheckVirtualAddress_function_00BA4D68.md) (function, `0x00BA4D68`)
- `0x00BA3DCD` → [ViZwCheckVirtualAddress](ViZwCheckVirtualAddress_function_00BA4D68.md) (function, `0x00BA4D68`)
- `0x00BA3DD9` → [ViZwCheckObjectAttributes](ViZwCheckObjectAttributes_function_00BA4C80.md) (function, `0x00BA4C80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BA3D90  40 53                           push rbx
00BA3D92  48 83 EC 20                     sub rsp, 0x20
00BA3D96  48 8B D9                        mov rbx, rcx
00BA3D99  E8 16 10 00 00                  call 0x140ba4db4
00BA3D9E  85 C0                           test eax, eax
00BA3DA0  74 3C                           je 0x140ba3dde
00BA3DA2  48 8B 13                        mov rdx, qword ptr [rbx]
00BA3DA5  48 8B 4B 48                     mov rcx, qword ptr [rbx + 0x48]
00BA3DA9  E8 BA 0F 00 00                  call 0x140ba4d68
00BA3DAE  48 8B 13                        mov rdx, qword ptr [rbx]
00BA3DB1  48 8B 4B 28                     mov rcx, qword ptr [rbx + 0x28]
00BA3DB5  E8 AE 0F 00 00                  call 0x140ba4d68
00BA3DBA  48 8B 13                        mov rdx, qword ptr [rbx]
00BA3DBD  48 8B 4B 18                     mov rcx, qword ptr [rbx + 0x18]
00BA3DC1  E8 A2 0F 00 00                  call 0x140ba4d68
00BA3DC6  48 8B 13                        mov rdx, qword ptr [rbx]
00BA3DC9  48 8B 4B 10                     mov rcx, qword ptr [rbx + 0x10]
00BA3DCD  E8 96 0F 00 00                  call 0x140ba4d68
00BA3DD2  48 8B 13                        mov rdx, qword ptr [rbx]
00BA3DD5  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
00BA3DD9  E8 A2 0E 00 00                  call 0x140ba4c80
00BA3DDE  48 83 C4 20                     add rsp, 0x20
00BA3DE2  5B                              pop rbx
00BA3DE3  C3                              ret
00BA3DE4  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VfZwAlpcAcceptConnectPort_Entry(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = ViZwShouldCheck(a1, a2, a3, a4);
    if ((unsigned int)(result) != 0) {
        a2 = *(unsigned __int64 *)(a1);
        a1 = *(unsigned __int64 *)(a1 + 72);
        result = ViZwCheckVirtualAddress(a1, a2, a3, a4);
        a2 = *(unsigned __int64 *)(a1);
        a1 = *(unsigned __int64 *)(a1 + 40);
        result = ViZwCheckVirtualAddress(a1, a2, a3, a4);
        a2 = *(unsigned __int64 *)(a1);
        a1 = *(unsigned __int64 *)(a1 + 24);
        result = ViZwCheckVirtualAddress(a1, a2, a3, a4);
        a2 = *(unsigned __int64 *)(a1);
        a1 = *(unsigned __int64 *)(a1 + 16);
        result = ViZwCheckVirtualAddress(a1, a2, a3, a4);
        a2 = *(unsigned __int64 *)(a1);
        a1 = *(unsigned __int64 *)(a1 + 48);
        result = ViZwCheckObjectAttributes(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t VfZwAlpcAcceptConnectPort_Entry(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = ViZwShouldCheck(Arg1, a2, a3, a4);
    if ((uint32_t)(result) != 0) {
        a2 = *(uint64_t *)(arg1);
        Arg1 = *(uint64_t *)(arg1 + 0x48);
        result = ViZwCheckVirtualAddress(Arg1, a2, a3, a4);
        a2 = *(uint64_t *)(arg1);
        Arg1 = *(uint64_t *)(arg1 + 0x28);
        result = ViZwCheckVirtualAddress(Arg1, a2, a3, a4);
        a2 = *(uint64_t *)(arg1);
        Arg1 = *(uint64_t *)(arg1 + 0x18);
        result = ViZwCheckVirtualAddress(Arg1, a2, a3, a4);
        a2 = *(uint64_t *)(arg1);
        Arg1 = *(uint64_t *)(arg1 + 0x10);
        result = ViZwCheckVirtualAddress(Arg1, a2, a3, a4);
        a2 = *(uint64_t *)(arg1);
        Arg1 = *(uint64_t *)(arg1 + 0x30);
        result = ViZwCheckObjectAttributes(Arg1, a2, a3, a4);
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
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x28` | `64` | `R` |
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg1` | `+ 0x48` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00BA3D90&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BA3D90[BB_00BA3D90]
  bb_00BA3DA2[BB_00BA3DA2]
  bb_00BA3DDE[BB_00BA3DDE]
  bb_00BA3DE4[BB_00BA3DE4]
  bb_00BA3D90 -->|branch| bb_00BA3DDE
  bb_00BA3D90 -->|fallthrough| bb_00BA3DA2
  bb_00BA3DA2 -->|flow| bb_00BA3DDE
```

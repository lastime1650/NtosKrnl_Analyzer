# KeReinitializeAffinityEx

- RVA: `0x00444E40`–`0x00444E68` (길이 `40` bytes)
- VA: `0x0000000140444E40`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `13`개 명령, `40/40` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00444E57` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00444E40  40 53                           push rbx
00444E42  48 83 EC 20                     sub rsp, 0x20
00444E46  44 0F B7 01                     movzx r8d, word ptr [rcx]
00444E4A  48 8B D9                        mov rbx, rcx
00444E4D  49 C1 E0 03                     shl r8, 3
00444E51  48 83 C1 08                     add rcx, 8
00444E55  33 D2                           xor edx, edx
00444E57  E8 E4 1D 28 00                  call 0x1406c6c40
00444E5C  66 C7 03 01 00                  mov word ptr [rbx], 1
00444E61  48 83 C4 20                     add rsp, 0x20
00444E65  5B                              pop rbx
00444E66  C3                              ret
00444E67  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KeReinitializeAffinityEx(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    a3 = (*(unsigned __int16 *)(a1)) << (3);
    a1 = (a1) + (8);
    a2 = 0;
    result = memset(a1, a2, a3, a4);
    *(unsigned __int16 *)(a1) = 1;
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KeReinitializeAffinityEx(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    a3 = (*(uint16_t *)(arg1)) << (3);
    Arg1 = (Arg1) + (8);
    Arg2 = 0;
    result = memset(Arg1, Arg2, a3, a4);
    *(uint16_t *)(arg1) = 1;
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `16` | `R` |
| `Arg1` | `+ 0x0` | `16` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00444E40&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00444E40[BB_00444E40]
  bb_00444E67[BB_00444E67]
```

# MiImageCfgRvaIteratorNext

- RVA: `0x0099FB70`–`0x0099FB8A` (길이 `26` bytes)
- VA: `0x000000014099FB70`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009B294`
- 디코드: `7`개 명령, `26/26` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [MiImageCfgRvaIteratorFirst](MiImageCfgRvaIteratorFirst_function_0099FB40.md) at `0x0099FB51`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x0099FB84` → [sub_0099FC2F](Unknown_function_0099FC2F.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0099FB70  48 83 EC 18                     sub rsp, 0x18
0099FB74  44 8B 4A 08                     mov r9d, dword ptr [rdx + 8]
0099FB78  45 33 D2                        xor r10d, r10d
0099FB7B  4C 8B D9                        mov r11, rcx
0099FB7E  41 8B C2                        mov eax, r10d
0099FB81  45 85 C9                        test r9d, r9d
0099FB84  0F 84 A5 00 00 00               je 0x14099fc2f
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiImageCfgRvaIteratorNext(__int64 a1, __int64 a2)
{
    __int64 v_r10;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (24);
    v_r10 = 0;
}
```

## 5. (Beta) C Style

```c
int64_t MiImageCfgRvaIteratorNext(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t local_r10;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (24);
    local_r10 = 0;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x8` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0099FB70&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0099FB70[BB_0099FB70]
```

# HalpApic1WriteRegister

- RVA: `0x0047B460`–`0x0047B470` (길이 `16` bytes)
- VA: `0x000000014047B460`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `5`개 명령, `16/16` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0047B460` → RVA `0x00E10440` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0047B460  48 8B 05 D9 4F 99 00            mov rax, qword ptr [rip + 0x994fd9]
0047B467  4C 63 C1                        movsxd r8, ecx
0047B46A  41 89 14 00                     mov dword ptr [r8 + rax], edx
0047B46E  C3                              ret
0047B46F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpApic1WriteRegister(int a1, int a2)
{
    *(unsigned int *)((int)(a1) + *(unsigned __int64 *)(v_rip + 10047449) * 1) = a2;
    return *(unsigned __int64 *)(v_rip + 10047449);
}
```

## 5. (Beta) C Style

```c
int64_t HalpApic1WriteRegister(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    *(uint32_t *)((int32_t)(arg1) + *(uint64_t *)(v_rip + 0x994FD9) * 1) = Arg2;
    return *(uint64_t *)(v_rip + 0x994FD9);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0 + rax*1` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0047B460&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0047B460[BB_0047B460]
  bb_0047B46F[BB_0047B46F]
```
